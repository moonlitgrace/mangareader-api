from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# scrapers
from .scrapers.popular_mangas import PopularScraper
from .scrapers.topten_mangas import TopTenScraper
# models
from .models import PopularMangaModel, BaseModel, TopTenMangaModel

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

@router.get("/most-viewed/{chart}")
async def get_most_viewed(chart: str):
	return None