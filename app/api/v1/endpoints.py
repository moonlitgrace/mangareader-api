from fastapi import APIRouter
from bs4 import BeautifulSoup

router = APIRouter()

BASE_URL = "https://mangareader.to/home"

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular")
async def get_trending_mangas():
	soup = BeautifulSoup(BASE_URL)
	print(soup)
	return None