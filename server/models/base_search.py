from typing import Dict, Optional
from pydantic import BaseModel


class BaseSearchModel(BaseModel):
    id: int
    manga_id: int
    title: str
    slug: str
    cover: str
    langs: list[str]
    chapters: Optional[Dict[str, str]]
