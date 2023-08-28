from typing import List, Optional
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

class TopTenMangaModel(BaseModel):
	id: int
	title: str
	slug: str
	cover: str
	synopsis: str
	chapters: dict[str, str]
	genres: list[str]

class MostViewedMangaModel(BaseModel):
	id: int
	rank: str
	title: str
	slug: str
	cover: str
	views: str
	langs: list[str]
	chapters: str
	volumes: Optional[str]
	genres: list[str]