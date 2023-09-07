from pydantic import BaseModel


class MangaModel(BaseModel):
    manga_id: int
    title: str
    alt_title: str
    slug: str
    type: str
    status: str
    published: str
    score: float
    views: int
    cover: str
    synopsis: str
    genres: list[str]
    authers: list[str]
    mangazines: list[str]
    chapters: list[dict[str, str]]
    volumes: list[dict[str, str]]