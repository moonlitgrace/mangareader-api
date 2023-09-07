from typing import Optional
from pydantic import BaseModel


class BaseSearchModel(BaseModel):
    id: int
    manga_id: int
    title: str
    slug: str
    cover: str
    langs: list[str]
    chapters: Optional[dict[str, str]]