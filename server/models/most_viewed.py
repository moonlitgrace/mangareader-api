from pydantic import BaseModel
from typing import List, Optional


class MostViewedMangaModel(BaseModel):
    id: int
    rank: str
    title: str
    slug: str
    cover: str
    views: str
    langs: List[str]
    chapters: str
    volumes: Optional[str]
    genres: List[str]
