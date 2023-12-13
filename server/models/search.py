from pydantic import BaseModel
from typing import List, Optional


class Search(BaseModel):
    title: str
    slug: str
    genres: List[str]
    langs: str
    cover_src: str
    chapters: Optional[float]
    volumes: Optional[float]
