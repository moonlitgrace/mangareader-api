from fastapi import APIRouter

from .scraper import PopularScraper, TopTenScraper
from .models import PopularMangaModel, TopTenMangaModel

router = APIRouter()

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular", response_model=list[PopularMangaModel])
async def get_trending_mangas() -> list[PopularMangaModel]:
	response = PopularScraper().scrape()
	return response

@router.get("/top-10", response_model=list[TopTenMangaModel])
async def get_top_ten() -> list[TopTenMangaModel]:
	response = TopTenScraper().scrape()
	return response

