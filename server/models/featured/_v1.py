from pydantic import BaseModel
from typing import List

from ..response import BaseResponseModel

class FeaturedMangaModal(BaseModel):
    title: str
    slug: str
    genres: List[str]
    cover: str
    synopsis: str
    chapter: float

class FeaturedResModal(BaseResponseModel):
    data: List[FeaturedMangaModal]