from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# scrapers
from .scrapers.popular import PopularScraper
from .scrapers.topten import TopTenScraper
from .scrapers.most_viewed import MostViewedScraper
# models
from .models import PopularMangaModel, BaseModel, TopTenMangaModel, MostViewedMangaModel

router = APIRouter()

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular", response_model=list[PopularMangaModel])
def get_trending_mangas():
	response =  PopularScraper().parse()
	return response

@router.get("/top-10", response_model=list[TopTenMangaModel])
async def get_top_ten():
	response = TopTenScraper().parse()
	return response

@router.get("/most-viewed/{chart}", response_model=list[MostViewedMangaModel])
async def get_most_viewed(chart: str):
	most_viewed_scraper = MostViewedScraper()

	if chart in most_viewed_scraper.CHARTS:
		response = most_viewed_scraper.parse(chart)
		return response
	else:
		message = "Parameter not acceptable."
		return JSONResponse(message, status_code=400)