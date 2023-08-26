from fastapi import APIRouter
from .scraper import PopularManagasScraper

router = APIRouter()

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular")
async def get_trending_mangas():
	managas = PopularManagasScraper().scrape()
	return managas