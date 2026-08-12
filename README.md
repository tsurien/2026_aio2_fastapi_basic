<div align="center">

# 2026 AIO2 FastAPI Basic

### FastAPI · API Server · Learning by Building

Python과 FastAPI를 이용해  
API 서버의 기본 구조와 웹 페이지 연결 방식을 직접 구현하며 학습하고 있습니다.

<br>

[![GitHub](https://img.shields.io/badge/GitHub-0D1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tsurien/2026_aio2_fastapi_basic)
[![FastAPI](https://img.shields.io/badge/FastAPI-0D1117?style=for-the-badge&logo=fastapi&logoColor=009688)](https://github.com/tsurien/2026_aio2_fastapi_basic)

</div>

---

## About

FastAPI를 사용해 **첫 API 서버를 만들고**,  
요청 경로에 따라 데이터를 반환하거나 HTML 페이지를 제공하는 흐름을 실습하고 있습니다.

단순한 `Hello World` 응답부터 시작해  
도서 데이터를 조회하고 검색하는 API와 정적 HTML 페이지를 연결하는 구조까지 직접 구현했습니다.

> request → route → response

---

## Focus

```text
FastAPI Application
        ↓
Routing
        ↓
Data Response
        ↓
Static Web Page
```

### FastAPI

`FastAPI` · `GET` · `Route` · `JSON Response`

`FastAPI()`로 애플리케이션을 생성하고  
경로별 함수를 연결하여 요청에 응답하는 기본 구조를 실습했습니다.

기본 예제에서는 `/` 경로를 통해 다음과 같은 메시지를 반환합니다.

```text
Hello World!!!
```

---

### API

`Health` · `Info` · `Books` · `Search` · `Detail`

도서 데이터를 기반으로 여러 API 엔드포인트를 구성했습니다.

```text
/health
/info
/api/books
/books/search
/books/{book_id}
```

`/health`에서는 서버 상태를 확인하고,  
`/info`에서는 API 이름과 버전 정보를 반환합니다.

도서 API에서는 전체 목록 조회,  
키워드를 이용한 제목 검색,  
도서 ID를 이용한 단건 조회를 실습했습니다.

---

### Static Pages

`StaticFiles` · `FileResponse` · `HTML`

FastAPI에서 `static` 폴더를 연결하고  
HTML 파일을 응답으로 반환하는 구조를 실습했습니다.

```text
static/
├── 01-status.html
├── 02-list.html
├── 03-detail.html
└── 04-search.html
```

도서 목록, 상세 조회, 검색 등의 기능을  
API뿐만 아니라 HTML 페이지와 연결하는 방식으로 구성했습니다.

---

### Web Basics

`HTML` · `CSS` · `JavaScript`

FastAPI 실습과 함께 기본적인 웹 문서 구조도 확인했습니다.

HTML 요소를 작성하고 CSS로 화면을 조정하며,  
JavaScript를 이용해 입력값을 읽어 화면에 표시하는 간단한 동작을 구현했습니다.

```text
사용자 입력
    ↓
JavaScript
    ↓
HTML 결과 변경
```

---

## Stack

<p>
  <img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=3776AB"/>
  <img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688"/>
  <img src="https://img.shields.io/badge/HTML5-0D1117?style=flat-square&logo=html5&logoColor=E34F26"/>
  <img src="https://img.shields.io/badge/CSS3-0D1117?style=flat-square&logo=css&logoColor=1572B6"/>
  <img src="https://img.shields.io/badge/JavaScript-0D1117?style=flat-square&logo=javascript&logoColor=F7DF1E"/>
  <img src="https://img.shields.io/badge/GitHub-0D1117?style=flat-square&logo=github&logoColor=white"/>
</p>

---

## Learning Log

### 01. First API Server

FastAPI 애플리케이션을 생성하고  
기본 경로에 함수를 연결하여 JSON 데이터를 반환하는 구조를 실습했습니다.

```text
GET /
→ Hello World!!!
```

---

### 02. API Status & Information

서버 상태와 API 정보를 확인할 수 있는 엔드포인트를 구현했습니다.

```text
GET /health
GET /info
```

---

### 03. Book List

Python 리스트에 저장된 도서 데이터를 이용해  
전체 도서 목록을 반환하는 API를 구현했습니다.

```text
GET /api/books
```

---

### 04. Book Search

`keyword` 값을 전달받아  
도서 제목에 해당 문자열이 포함되어 있는지 확인하고 결과를 반환하도록 구현했습니다.

```text
GET /books/search
```

---

### 05. Book Detail

URL에 전달된 `book_id` 값을 이용해  
특정 도서를 찾아 반환하는 기능을 구현했습니다.

```text
GET /books/{book_id}
```

일치하는 도서가 없을 경우에는 다음과 같은 결과를 반환하도록 작성했습니다.

```text
not found
```

---

### 06. HTML Page Connection

FastAPI에서 `FileResponse`를 이용해  
HTML 파일을 직접 반환하는 페이지를 구성했습니다.

```text
/books
/search
/book
```

API 데이터 처리와 웹 페이지가  
어떻게 연결될 수 있는지 확인하는 실습입니다.

---

## Project Structure

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

### `main.py`

도서 데이터를 기반으로 API와 HTML 페이지 경로를 구성한 메인 FastAPI 실습 파일입니다.

### `hello.py`

FastAPI 애플리케이션을 생성하고  
루트 경로에서 간단한 메시지를 반환하는 기본 실습 파일입니다.

### `hello.html`

기본적인 HTML 문서 구조와 태그를 확인하는 실습 파일입니다.

### `html_js_css.html`

HTML, CSS, JavaScript를 함께 사용해  
이름을 입력받고 화면에 결과를 표시하는 동작을 실습한 파일입니다.

### `static/`

FastAPI에서 제공하는 상태, 목록, 상세, 검색 관련 HTML 페이지가 들어 있습니다.

---

## Current Flow

```text
Client Request
      ↓
FastAPI Route
      ↓
Python Data / HTML File
      ↓
Response
```

현재 저장소에서는 FastAPI의 경로 처리와 데이터 응답부터  
정적 HTML 페이지 연결까지 단계적으로 실습하고 있습니다.

---

## Direction

현재는 복잡한 기능을 추가하기보다  
**API 서버가 요청을 받고 응답을 만드는 기본 흐름을 직접 구현하며 이해하는 것**에 집중하고 있습니다.

```text
create  →  route  →  request  →  response  →  connect
```

작은 API부터 직접 만들어보며  
Python 코드와 웹 페이지가 연결되는 구조를 학습하고 있습니다.

---

## Repository

**2026 AIO2 FastAPI Basic**

https://github.com/tsurien/2026_aio2_fastapi_basic

---

<div align="center">

### build the API. understand the flow.

`tsurien`

</div>
