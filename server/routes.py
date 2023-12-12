from fastapi import APIRouter
from .scrapers import MangaScraper

router = APIRouter()


@router.get(path="/kitsu/manga/")
async def manga():
    return "Hii"
