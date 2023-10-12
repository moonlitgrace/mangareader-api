from typing import Dict, List
from pydantic import BaseModel


class PopularMangaModel(BaseModel):
    id: int
    rank: str
    title: str
    slug: str
    cover: str
    rating: float
    langs: List[str]
    chapters: Dict[str, str]
    volumes: Dict[str, str]
