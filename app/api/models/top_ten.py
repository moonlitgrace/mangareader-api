from pydantic import BaseModel


class TopTenMangaModel(BaseModel):
    id: int
    title: str
    slug: str
    cover: str
    synopsis: str
    chapters: dict[str, str]
    genres: list[str]
