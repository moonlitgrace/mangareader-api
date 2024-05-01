from pydantic import BaseModel
from typing import List

from app.schemas import BaseResponse


# Featured Manga Model
class FeaturedManga(BaseModel):
    title: str
    slug: str
    genres: List[str]
    cover: str
    synopsis: str
    chapter: float

class FeaturedResponse(BaseResponse):
    data: List[FeaturedManga]

# Manga Model
class Manga(BaseModel):
    title: str
    slug: str
    alt_title: str
    genres: List[str]
    type: str
    rating: float
    authors: str
    published_date: str
    cover: str
    synopsis: str

# Search Model
class SearchManga(BaseModel):
    title: str
    slug: str
    genres: List[str]
    langs: List[str]
    cover: str
    chapters: float
    volumes: float


class SearchMangaResponse(BaseResponse):
    data: List[SearchManga]

# Trending Manga Model
class TrendingManga(BaseModel):
    title: str
    slug: str
    cover: str
    rating: float
    langs: List[str]
    chapters: float
    volumes: float


class TrendingResponse(BaseResponse):
    data: List[TrendingManga]
