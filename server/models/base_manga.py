from typing import Dict, List
from pydantic import BaseModel


class MangaModel(BaseModel):
    manga_id: int
    title: str
    alt_title: str
    slug: str
    type: str
    status: str
    published: str
    score: float
    views: int
    cover: str
    synopsis: str
    genres: List[str]
    authers: List[str]
    mangazines: List[str]
    chapters: List[Dict[str, str]]
    volumes: List[Dict[str, str]]
