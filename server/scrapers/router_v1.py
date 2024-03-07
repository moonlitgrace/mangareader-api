from fastapi import APIRouter

from ..scrapers.featured._v1 import FeaturedScraper
from ..scrapers.trending._v1 import TrendingScraper as v1TrendintScraper
from ..helpers.response import ResponseHelper

router = APIRouter()

@router.get("/featured")
async def featured():
    response = FeaturedScraper().scrape()
    return ResponseHelper.format_response(response)

@router.get("/trending")
async def trending():
    response = v1TrendintScraper().scrape()
    return ResponseHelper.format_response(response)