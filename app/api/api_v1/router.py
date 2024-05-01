from fastapi import APIRouter

from .scrapers.featured import FeaturedScraper
from .scrapers.trending import TrendingScraper
from .scrapers.manga import MangaScraper
from .scrapers.search import SearchScraper

from app.helpers import ResponseHelper

from .schemas import (
    FeaturedResponse,
    TrendingResponse,
    Manga as MangaModel,
    SearchMangaResponse,
)

router = APIRouter()


@router.get("/featured", response_model=FeaturedResponse)
async def featured():
    response = FeaturedScraper().build()
    return ResponseHelper.format_response(response)


@router.get("/trending", response_model=TrendingResponse)
async def trending():
    response = TrendingScraper().build()
    return ResponseHelper.format_response(response)


@router.get("/manga/{slug}", response_model=MangaModel)
async def manga(slug: str):
    response = MangaScraper(slug).build()
    return response


@router.get("/search/{query}", response_model=SearchMangaResponse)
async def search(query: str):
    response = SearchScraper(query).build()
    return ResponseHelper.format_response(response)
