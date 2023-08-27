from fastapi import APIRouter, responses

from .scraper import PopularScraper, TopTenScraper, MostViewedScraper
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

@router.get("/most-viewed/{local_date}")
async def get_most_viewed(local_date: str):
	if local_date == "today":
		response = MostViewedScraper().scrape_today()
		return response
	elif local_date == "week":
		response = MostViewedScraper().scrape_week()
		return "Week"
	elif local_date == "month":
		response = MostViewedScraper().scrape_month()
		return "Month"