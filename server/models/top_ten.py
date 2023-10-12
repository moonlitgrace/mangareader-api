from typing import Dict, List
from pydantic import BaseModel


class TopTenMangaModel(BaseModel):
    id: int
    title: str
    slug: str
    cover: str
    synopsis: str
    chapters: Dict[str, str]
    genres: List[str]
