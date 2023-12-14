from typing import List
from pydantic import BaseModel


class Manga(BaseModel):
    title: str
    alt_title: str
    type: str
    genres: List[str]
    status: str
    score: float
    cover_src: str
    synopsis: str
