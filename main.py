from fastapi import FastAPI, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# -----------------------------
# Pydantic 모델
# -----------------------------

class Publisher(BaseModel):
    name: str
    city: str = "고양"

class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=50)
    year: int = Field(ge=1900, le=2026)
    tags: list[str] = Field(default_factory=list)
    publisher: Publisher | None = None

    def strip_title(cls, v: str) -> str:
        v = v.strip()
        # 공백 문자열 체크
        if not v:
            raise ValueError("제목은 필수입력입니다.(공백안됨)")
        return v

class BookResponse(BookCreate):
    id: int

# -----------------------------
# FastAPI 앱 생성
# -----------------------------

app = FastAPI()

# -----------------------------
# static 폴더 연결
# -----------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------------
# 도서 데이터
# -----------------------------

books = [
    {"id": 1, "title": "파이썬 입문", "author": "김철수", "year": 2021},
    {"id": 2, "title": "FastAPI 실전", "author": "이영희", "year": 2023},
    {"id": 3, "title": "파이썬 웹개발", "author": "김철수", "year": 2022},
    {"id": 4, "title": "데이터 분석 기초", "author": "박민수", "year": 2020},
    {"id": 5, "title": "FastAPI로 배우는 백엔드", "author": "이영희", "year": 2024},
]

# -----------------------------
# 메인 페이지
# -----------------------------

@app.get("/")
def index():
    return FileResponse("static/00-index.html")

# -----------------------------
# 서버 상태 확인
# -----------------------------

@app.get("/health")
def health():
    return {"status": "healthy"}

# -----------------------------
# API 정보
# -----------------------------

@app.get("/info")
def info():
    return {
        "name": "도서 관리 API",
        "version": "0.1.0"
    }

# -----------------------------
# 02 도서 목록 페이지
# -----------------------------

@app.get("/books")
def books_page():
    return FileResponse("static/02-list.html")

# -----------------------------
# 도서 목록 API
# -----------------------------

@app.get("/list", response_model=list[BookResponse])
def get_books():
    return books

# -----------------------------
# 03 도서 단건 조회 페이지
# -----------------------------

@app.get("/book")
def book_page():
    return FileResponse("static/03-detail.html")

# -----------------------------
# 04 도서 검색 페이지
# -----------------------------

@app.get("/search")
def search_page():
    return FileResponse("static/04-search.html")

# -----------------------------
# 도서 검색 API
# -----------------------------

@app.get("/books/search")
def search_books(keyword: str):
    result = []

    for book in books:
        if keyword in book["title"]:
            result.append(book)

    return result

# -----------------------------
# 05 저자 필터 페이지
# -----------------------------

@app.get("/filter")
def filter_page():
    return FileResponse("static/05-filter.html")

# -----------------------------
# 저자 필터 · 정렬 API
# -----------------------------

@app.get("/books/filter")
def filter_books(keyword: str = "", sort: str = ""):
    result = books

    # 리스트 컴프리헨션
    result = [b for b in result if b["author"] == keyword]

    if sort == "year":
        result = sorted(result, key=lambda b: b["year"])

    return result

# -----------------------------
# 06 페이지네이션 페이지
# -----------------------------

@app.get("/page")
def page_view():
    return FileResponse("static/06-page.html")

# -----------------------------
# 페이지네이션 API
# -----------------------------

@app.get("/books/page")
def page_books(skip: int = 0, limit: int = 2):
    return books[skip:skip + limit]

# -----------------------------
# 특정 도서 조회 API
# -----------------------------

@app.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int):
    for book in books:
        if book_id == book["id"]:
            return book

    raise HTTPException(
        status_code=404,
        detail="도서를 찾을 수 없습니다."
    )

# -----------------------------
# 도서 등록 API
# -----------------------------

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    for b in books:
        if b['title'] == book.title :
            raise HTTPException(status_code=409, detail="이미 등록된 제목입니다.")
    new_id = max([b["id"] for b in books], default=0) + 1
    new_book = {"id": new_id, **book.model_dump()}
    books.append(new_book)
    return new_book

# -----------------------------
# 테스트 시나리오
# -----------------------------

# 책 등록
# ↓
# 목록 조회
# ↓
# 책 검색
#
# 습관을 들이자!