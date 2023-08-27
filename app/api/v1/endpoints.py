from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .scrapers.popular_mangas import PopularScraper

router = APIRouter()

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular")
async def get_trending_mangas():
	response =  PopularScraper().parse()
	return response

@router.get("/top-10")
async def get_top_ten():
	return None

@router.get("/most-viewed/{chart}")
async def get_most_viewed(chart: str):
	return None