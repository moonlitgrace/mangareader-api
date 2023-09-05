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

class SearchMangaModel(BaseModel):
	id: int
	manga_id: int
	title: str
	slug: str
	cover: str
	langs: list[str]
	chapters: Optional[dict[str, str]]