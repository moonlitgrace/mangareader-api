from pydantic import BaseModel


class PopularMangaModel(BaseModel):
    id: int
    rank: str
    title: str
    slug: str
    cover: str
    rating: float
    langs: list[str]
    chapters: dict[str, str]
    volumes: dict[str, str]