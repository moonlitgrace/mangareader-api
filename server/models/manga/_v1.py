from pydantic import BaseModel
from typing import List

class MangaModel(BaseModel):
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