from pydantic import BaseModel
from typing import List, Optional


class Search(BaseModel):
    title: str
    slug: str
    genres: List[str]
    cover: str
    chapters: Optional[float]
    provider_url: str
    manga_url: str
