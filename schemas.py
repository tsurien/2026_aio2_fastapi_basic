from pydantic import BaseModel, Field

# -----------------------------
# 출판사 정보
class Publisher(BaseModel):
    name: str = Field(
        min_length=1, max_length=100,
        description="출판사 이름",
        examples=["한빛미디어"],
    )
    city: str = Field(
        default="고양",
        description="출판사 위치",
        examples=["서울"],
    )

# -----------------------------
# 도서 등록 요청 정보
class BookCreate(BaseModel):
    title: str = Field(
        min_length=1, max_length=100,
        description="도서 제목",
        examples=["처음 시작하는 FastAPI"],
    )
    author: str = Field(
        min_length=1, max_length=50,
        description="도서 저자",
        examples=["김민수"],
    )
    year: int = Field(
        ge=1900, le=2026,
        description="출판 연도",
        examples=[2024],
    )
    tags: list[str] = Field(
        default_factory=list,
        description="도서 태그 목록",
        examples=[["파이썬", "웹 개발"]],
    )
    publisher: Publisher | None = Field(
        default=None,
        description="출판사 정보",
        examples=[{"name": "한빛미디어", "city": "서울"}],
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "처음 시작하는 FastAPI",
                "author": "김민수",
                "year": 2024,
                "tags": ["파이썬", "웹 개발"],
                "publisher": {
                    "name": "한빛미디어",
                    "city": "서울"
                }
            }
        }
    }

    def strip_title(cls, v: str) -> str:
        v = v.strip()
        # 공백 문자열 체크
        if not v:
            raise ValueError("제목은 필수입력입니다.(공백안됨)")
        return v

# -----------------------------
# 도서 응답 정보
class BookResponse(BookCreate):
    id: int = Field(
        description="도서 식별 번호",
        examples=[1],
    )

# -----------------------------
# 날씨 API 응답 정보
class WeatherResponse(BaseModel):
    latitude: float = Field(
        description="위도",
        examples=[37.5665],
    )
    longitude: float = Field(
        description="경도",
        examples=[126.9780],
    )
    temperature: float = Field(
        description="현재 기온",
        examples=[24.5],
    )
    time: str = Field(
        description="관측 시간",
        examples=["2026-08-18T17:00"],
    )

# -----------------------------
# Google Books 도서 정보
class GoogleBooks(BaseModel):
    title: str = Field(
        description="도서 제목",
        examples=["파이썬으로 배우는 웹 개발"],
    )
    authors: list[str] = Field(
        default_factory=list,
        description="도서 저자 목록",
        examples=[["김민수", "이서연"]],
    )
    published_date: str = Field(
        default="",
        description="출판일",
        examples=["2024-03-15"],
    )

# -----------------------------
# 외부 API 도서 정보
class ExternalBook(BaseModel):
    title: str = Field(
        description="도서 제목",
        examples=["FastAPI로 시작하는 백엔드 개발"],
    )
    authors: list[str] = Field(
        default_factory=list,
        description="도서 저자 목록",
        examples=[["박지훈"]],
    )
    published_date: str = Field(
        default="",
        description="출판일",
        examples=["2025-05-20"],
    )
