from typing import List
from pydantic import BaseModel


class Manga(BaseModel):
    title: str
    alt_title: str
    status: str
    author: str
    score: float
    genres: List[str]
    cover: str
    synopsis: str
    provider_url: str
    manga_url: str
