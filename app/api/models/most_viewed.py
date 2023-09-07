from pydantic import BaseModel
from typing import Optional


class MostViewedMangaModel(BaseModel):
    id: int
    rank: str
    title: str
    slug: str
    cover: str
    views: str
    langs: list[str]
    chapters: str
    volumes: Optional[str]
    genres: list[str]
