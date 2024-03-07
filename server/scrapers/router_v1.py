from fastapi import APIRouter

from ..scrapers.featured._v1 import FeaturedScraper
from ..scrapers.trending._v1 import TrendingScraper as v1TrendintScraper
from ..helpers.response import ResponseHelper
from ..models.featured import FeaturedResModal
from ..models.trending import TrendingResModel

router = APIRouter()

@router.get("/featured", response_model=FeaturedResModal)
async def featured():
    response = FeaturedScraper().scrape()
    return ResponseHelper.format_response(response)

@router.get("/trending", response_model=TrendingResModel)
async def trending():
    response = v1TrendintScraper().scrape()
    return ResponseHelper.format_response(response)