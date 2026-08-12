<div align="center">

# 2026 AIO2 FastAPI Basic

### Python → API → Web

FastAPI로 요청을 받고, 데이터를 반환하고,  
HTML 페이지까지 연결해보는 웹 API 기초 실습

<br>

`FastAPI` · `REST API` · `HTML` · `CSS` · `JavaScript`

</div>

---

## What I Built

```text
Client
  ↓
FastAPI
  ├─ JSON API
  │   ├─ Health Check
  │   ├─ Book List
  │   ├─ Book Search
  │   └─ Book Detail
  │
  └─ HTML Page
      ├─ Status
      ├─ List
      ├─ Detail
      └─ Search
```

단순한 `Hello World`에서 시작해  
**도서 데이터를 조회하는 API와 브라우저 화면을 연결하는 구조**까지 구현했습니다.

---

## API

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | 기본 응답 |
| `GET` | `/health` | 서버 상태 확인 |
| `GET` | `/info` | API 정보 |
| `GET` | `/api/books` | 전체 도서 조회 |
| `GET` | `/books/search` | 도서 검색 |
| `GET` | `/books/{book_id}` | 도서 상세 조회 |

```text
GET /api/books
        ↓
Python Book Data
        ↓
JSON Response
```

---

## Web

Fast
