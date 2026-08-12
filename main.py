from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()

# static 폴더 연결
app.mount("/static", StaticFiles(directory="static"), name="static")


# 도서 데이터
books = [
    {"id": 1, "title": "파이썬 입문", "author": "김철수", "year": 2021},
    {"id": 2, "title": "FastAPI 실전", "author": "이영희", "year": 2023},
    {"id": 3, "title": "파이썬 웹개발", "author": "김철수", "year": 2022},
    {"id": 4, "title": "데이터 분석 기초", "author": "박민수", "year": 2020},
    {"id": 5, "title": "FastAPI로 배우는 백엔드", "author": "이영희", "year": 2024},
]


# 서버 상태 확인
@app.get("/health")
def health():
    return {"status": "healthy"}


# API 정보
@app.get("/info")
def info():
    return {
        "name": "도서 관리 API",
        "version": "0.1.0"
    }


# 도서 목록 페이지
@app.get("/books")
def books_page():
    return FileResponse("static/02-list.html")


# 도서 목록 API
@app.get("/api/books")
def get_books():
    return books


# 도서 검색 페이지
@app.get("/search")
def search_page():
    return FileResponse("static/04-search.html")


# 도서 검색 API
@app.get("/books/search")
def search_books(keyword: str):
    result = []

    for book in books:
        if keyword in book["title"]:
            result.append(book)

    return result


# 특정 도서 조회 API
@app.get("/books/{book_id}")
def read_book(book_id: int):
    for book in books:
        if book_id == book["id"]:
            return book

    return {"error": "not found"}

# 도서 단건 조회 페이지
@app.get("/book")
def book_page():
    return FileResponse("static/03-detail.html")

# 특정 도서 조회 API
@app.get("/books/{book_id}")
def read_book(book_id: int):
    for book in books:
        if book_id == book["id"]:
            return book

    return {"error": "not found"}