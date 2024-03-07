from pydantic import BaseModel
from typing import List

from ..models.response import BaseResponseModel

class TrendingMangaModel(BaseModel):
    title: str
    slug: str
    cover: str
    rating: float
    langs: List[str]
    chapters: float
    volumes: float

class TrendingResModel(BaseResponseModel):
    data: List[TrendingMangaModel]