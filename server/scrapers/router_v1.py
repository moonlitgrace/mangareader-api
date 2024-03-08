from fastapi import APIRouter

from ..scrapers.featured._v1 import FeaturedScraper
from ..scrapers.trending._v1 import TrendingScraper
from ..scrapers.manga._v1 import MangaScraper

from ..helpers.response import ResponseHelper

from ..models.featured._v1 import FeaturedResModal
from ..models.trending._v1 import TrendingResModel
from ..models.manga._v1 import MangaModel

router = APIRouter()

@router.get("/featured", response_model=FeaturedResModal)
async def featured():
    response = FeaturedScraper().scrape()
    return ResponseHelper.format_response(response)

@router.get("/trending", response_model=TrendingResModel)
async def trending():
    response = TrendingScraper().scrape()
    return ResponseHelper.format_response(response)

@router.get("/manga/{query}", response_model=MangaModel)
async def manga(query: str):
    response = MangaScraper(query).scrape()
    return response