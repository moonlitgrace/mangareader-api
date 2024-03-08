from pydantic import BaseModel
from typing import List

from ..response import BaseResponseModel

class SearchMangaModel(BaseModel):
    title: str
    slug: str
    genres: List[str]
    langs: List[str]
    cover: str
    chapters: float
    volumes: float

class SearchMangaResModel(BaseResponseModel):
    data: List[SearchMangaModel]