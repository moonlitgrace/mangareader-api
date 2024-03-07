from fastapi import APIRouter

from ..scrapers.featured._v1 import FeaturedScraper
from ..helpers.response import ResponseHelper

router = APIRouter()

@router.get("/featured")
async def featured():
    response = FeaturedScraper().scrape()
    return ResponseHelper.format_response(response)
    # return {
    #     "count": len(response),
    #     "next": None,
    #     "prev": None,
    #     "result": response,
    # }