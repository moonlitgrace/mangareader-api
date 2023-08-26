from fastapi import APIRouter
from .scraper import PopularScraper, TopTenScraper

router = APIRouter()

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular")
async def get_trending_mangas():
	response = PopularScraper().scrape()
	return response

@router.get("/top-10")
async def get_top_ten():
	response = TopTenScraper().scrape()
	return response