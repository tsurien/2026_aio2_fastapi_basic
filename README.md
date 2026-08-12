<div align="center">

# 2026 AIO2 FastAPI Basic

### Python → API → Web

FastAPI로 요청을 받고, 데이터를 반환하고,  
HTML 페이지까지 연결해보는 웹 API 기초 실습

<br>

[![GitHub](https://img.shields.io/badge/GitHub-0D1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tsurien/2026_aio2_fastapi_basic)
[![Email](https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=EA4335)](mailto:tsurien@gmail.com)

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

FastAPI의 `StaticFiles`와 `FileResponse`를 이용해  
API뿐 아니라 HTML 페이지도 연결했습니다.

```text
static/
├── 01-status.html
├── 02-list.html
├── 03-detail.html
└── 04-search.html
```

`HTML` · `CSS` · `JavaScript`를 함께 사용해  
API에서 다룬 데이터를 웹 화면으로 확장하는 흐름을 확인했습니다.

---

## Structure

```text
2026_aio2_fastapi_basic/
│
├── main.py
├── hello.py
├── hello.html
├── html_js_css.html
│
└── static/
    ├── 01-status.html
    ├── 02-list.html
    ├── 03-detail.html
    └── 04-search.html
```

`hello.py`에서 FastAPI의 가장 작은 실행 구조를 확인하고,  
`main.py`에서 라우팅과 도서 API, HTML 응답으로 기능을 확장했습니다.

---

## Stack

<p>
  <img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=3776AB"/>
  <img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688"/>
  <img src="https://img.shields.io/badge/HTML5-0D1117?style=flat-square&logo=html5&logoColor=E34F26"/>
  <img src="https://img.shields.io/badge/CSS3-0D1117?style=flat-square&logo=css3&logoColor=1572B6"/>
  <img src="https://img.shields.io/badge/JavaScript-0D1117?style=flat-square&logo=javascript&logoColor=F7DF1E"/>
</p>

---

## Key Takeaway

```text
route
  → request
    → data
      → response
        → browser
```

FastAPI의 핵심 흐름을 작은 API부터 직접 구현하며 확인하는 저장소입니다.

---

<div align="center">

### from Python code to web API.

[View Repository](https://github.com/tsurien/2026_aio2_fastapi_basic)

</div>
