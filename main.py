from fastapi import FastAPI, status, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx

from schemas import ExternalBook, WeatherResponse, BookResponse, BookCreate, GoogleBooks
from external_api import fetch_weather, fetch_books, load_fallback_books

# -----------------------------
# Swagger UI에서 엔드포인트를 기능별로 구분하기 위한 태그 정보
tags_metadata = [
    {"name": "도서", "description": "도서 등록, 조회, 검색"},
    {"name": "외부 연동", "description": "Google Books와 날씨 API 연동"},
    {"name": "시스템", "description": "서버 상태 및 API 정보 확인"},
    {"name": "학습용", "description": "FastAPI 동작 학습용"},
]

# -----------------------------
# FastAPI 애플리케이션 기본 정보 및 Swagger 문서 설정
app = FastAPI(
    title="도서 관리 API !!",
    description="도서를 등록·조회하고 외부 검색으로 정보를 가져오는 API",
    version="1.0.0",
    contact={"name": "성관현", "email": "^-^@example.com"},
    openapi_tags=tags_metadata,
)

# -----------------------------
# HTML, CSS 등 정적 파일을 /static 경로에서 사용할 수 있도록 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------------
# 실습에서 사용할 임시 도서 데이터
books = [
    {"id": 1, "title": "파이썬 입문", "author": "김철수", "year": 2021},
    {"id": 2, "title": "FastAPI 실전", "author": "이영희", "year": 2023},
    {"id": 3, "title": "파이썬 웹개발", "author": "김철수", "year": 2022},
    {"id": 4, "title": "데이터 분석 기초", "author": "박민수", "year": 2020},
    {"id": 5, "title": "FastAPI로 배우는 백엔드", "author": "이영희", "year": 2024},
]

# -----------------------------
# 메인 페이지
@app.get("/", tags=["시스템"], summary="메인 페이지")
def index():
    """
    메인 페이지를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return FileResponse("static/00-index.html")

# -----------------------------
# 서버가 정상적으로 동작하는지 확인하는 상태 확인 API
@app.get("/health", tags=["시스템"], summary="서버 상태 확인")
def health():
    """
    서버 상태를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return {"status": "healthy"}

# -----------------------------
# 현재 API의 이름과 버전 정보를 반환
@app.get("/info", tags=["시스템"], summary="API 정보 조회")
def info():
    """
    API 이름과 버전 정보를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return {
        "name": "도서 관리 API",
        "version": "0.1.0"
    }

# -----------------------------
# 등록된 도서 목록을 보여주는 HTML 페이지
@app.get("/books", tags=["도서"], summary="도서 목록 페이지")
def books_page():
    """
    도서 목록 페이지를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return FileResponse("static/02-list.html")

# -----------------------------
# 등록된 전체 도서 데이터를 반환하는 API
@app.get("/list", response_model=list[BookResponse], tags=["도서"], summary="도서 목록 조회")
def get_books():
    """
    전체 도서 목록을 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return books

# -----------------------------
# 특정 도서를 조회할 수 있는 HTML 페이지
@app.get("/book", tags=["도서"], summary="도서 단건 조회 페이지")
def book_page():
    """
    도서 단건 조회 페이지를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return FileResponse("static/03-detail.html")

# -----------------------------
# 도서 제목 검색 기능을 사용하는 HTML 페이지
@app.get("/search", tags=["도서"], summary="도서 검색 페이지")
def search_page():
    """
    도서 검색 페이지를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return FileResponse("static/04-search.html")

# -----------------------------
# 입력한 keyword가 제목에 포함된 도서를 검색
@app.get("/books/search", tags=["도서"], summary="도서 검색")
def search_books(keyword: str):
    """
    도서 제목에 키워드가 포함된 도서를 검색합니다.

    - **keyword**: 도서 제목에서 검색할 문자열

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    result = []

    for book in books:
        if keyword in book["title"]:
            result.append(book)

    return result

# -----------------------------
# 저자를 기준으로 도서를 필터링하는 HTML 페이지
@app.get("/filter", tags=["도서"], summary="저자 필터 페이지")
def filter_page():
    """
    저자 필터 페이지를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return FileResponse("static/05-filter.html")

# -----------------------------
# 저자명으로 도서를 필터링하고 필요하면 출판 연도로 정렬
@app.get("/books/filter", tags=["도서"], summary="저자 필터 및 정렬")
def filter_books(keyword: str = "", sort: str = ""):
    """
    저자를 기준으로 도서를 필터링하고 조건에 따라 정렬합니다.

    - **keyword**: 필터링할 저자 이름
    - **sort**: 정렬 기준 문자열

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    result = books
    # 입력한 저자 이름과 정확히 일치하는 도서만 추출
    result = [b for b in result if b["author"] == keyword]

    if sort == "year":
        result = sorted(result, key=lambda b: b["year"])
    return result

# -----------------------------
# 페이지네이션 기능을 확인하기 위한 HTML 페이지
@app.get("/page", tags=["도서"], summary="페이지네이션 페이지")
def page_view():
    """
    페이지네이션 페이지를 반환합니다.

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return FileResponse("static/06-page.html")

# -----------------------------
# skip부터 limit 개수만큼 도서 데이터를 잘라서 반환
@app.get("/books/page", tags=["도서"], summary="도서 페이지네이션")
def page_books(skip: int = 0, limit: int = 2):
    """
    지정한 범위의 도서 목록을 반환합니다.

    - **skip**: 목록에서 건너뛸 도서 수
    - **limit**: 반환할 도서 수

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return books[skip:skip + limit]

# -----------------------------
# 요청받은 도서 정보를 검증한 뒤 새로운 ID를 생성하여 등록
@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED,
          tags=["도서"], summary="도서 등록", response_description="등록된 도서 정보",
          responses={409: {"description": "이미 등록된 제목입니다."}})
def create_book(book: BookCreate):
    """
    새 도서를 등록합니다.

    - **book**: 등록할 도서 정보

    같은 제목의 도서가 존재하면 409 오류가 발생합니다.
    """
    for b in books:
        if b["title"] == book.title:
            raise HTTPException(status_code=409,
                                detail="이미 등록된 제목입니다.")

    new_id = max([b["id"] for b in books], default=0) + 1
    new_book = {"id": new_id, **book.model_dump()}
    books.append(new_book)
    return new_book

# -----------------------------
# 위도와 경도를 외부 날씨 API에 전달하여 현재 날씨 조회
@app.get("/weather", response_model=WeatherResponse, tags=["외부 연동"], summary="현재 날씨 조회")
async def weather(latitude: float = 36.8, longitude: float = 127.1):
    """
    위도와 경도를 사용하여 날씨 정보를 조회합니다.

    - **latitude**: 조회할 위치의 위도
    - **longitude**: 조회할 위치의 경도

    명시적으로 발생시키는 HTTP 오류 상태 코드는 없습니다.
    """
    return await fetch_weather(latitude, longitude)

# -----------------------------
# Google Books API를 호출하고 외부 API 오류 발생 시 fallback 데이터 처리
@app.get("/books/external", response_model=list[ExternalBook], tags=["외부 연동"],
         summary="외부 도서 검색",
         responses={
             502: {"description": "외부 API가 오류를 반환했거나 연결할 수 없습니다"},
             504: {"description": "외부 API 응답이 지연됩니다"}
         })
async def search_external_books(keyword: str, limit: int = 5, fallback: bool = False):
    """
    외부 API를 사용하여 도서를 검색합니다.

    - **keyword**: 검색할 도서 키워드
    - **limit**: 검색 결과 개수
    - **fallback**: 외부 API 오류 발생 시 대체 데이터를 반환할지 여부

    외부 API 요청 실패 상황에 따라 502 또는 504 오류가 발생할 수 있습니다.
    """
    try:
        return await fetch_books(keyword, limit)

    except httpx.TimeoutException:
        if fallback:
            return load_fallback_books()
        raise HTTPException(status_code=504,
                            detail="외부 API 응답이 지연됩니다")

    except httpx.HTTPStatusError:
        if fallback:
            return load_fallback_books()
        raise HTTPException(status_code=502,
                            detail="외부 API가 오류를 반환했습니다")

    except httpx.RequestError:
        if fallback:
            return load_fallback_books()
        raise HTTPException(status_code=502,
                            detail="외부 API에 연결할 수 없습니다")

# -----------------------------
# 외부 API에서 조회한 도서 정보를 내부 books 목록 형식으로 변환하여 등록
@app.post("/books/from-external", response_model=BookResponse, status_code=201,
          tags=["도서"], summary="외부 도서 등록",
          responses={409: {"description": "이미 등록된 제목입니다"}})
def create_from_external(book: ExternalBook):
    """
    외부 검색 결과의 도서 정보를 도서 목록에 등록합니다.

    - **book**: 등록할 외부 도서 정보

    같은 제목의 도서가 존재하면 409 오류가 발생합니다.
    """
    for b in books:
        if b["title"] == book.title:
            raise HTTPException(status_code=409,
                                detail="이미 등록된 제목입니다")

    year = 2000
    if book.published_date[:4].isdigit():
        year = int(book.published_date[:4])

    new_id = max([b["id"] for b in books], default=0) + 1
    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.authors[0] if book.authors else "미상",
        "year": year,
        "tags": ["외부검색"],
        "publisher": None,
    }
    books.append(new_book)
    return new_book

# -----------------------------
# 동적 경로 /books/{book_id}는 다른 /books/... 경로보다 마지막에 선언
@app.get("/books/{book_id}", response_model=BookResponse, tags=["도서"],
         summary="도서 단건 조회",
         responses={404: {"description": "도서를 찾을 수 없습니다."}})
def read_book(book_id: int):
    """
    도서 ID를 사용하여 특정 도서를 조회합니다.

    - **book_id**: 조회할 도서의 ID

    해당 ID의 도서가 존재하지 않으면 404 오류가 발생합니다.
    """
    for book in books:
        if book_id == book["id"]:
            return book

    raise HTTPException(status_code=404, detail="도서를 찾을 수 없습니다.")
