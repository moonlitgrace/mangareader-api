from fastapi import APIRouter

from .scrapers.featured import FeaturedScraper
from .scrapers.trending import TrendingScraper
from .scrapers.manga import MangaScraper
from .scrapers.search import SearchScraper

from mangareader_api.helpers import ResponseHelper

from .schemas import (
    FeaturedResponse,
    TrendingResponse,
    Manga as MangaModel,
    SearchMangaResponse,
)

router = APIRouter()


@router.get(
    "/featured",
    response_model=FeaturedResponse,
    description="Retrieve a list of featured mangas titles. These titles represent a curated selection of popular or noteworthy mangas currently available on MangaReader.",
)
async def featured():
    response = FeaturedScraper().build()
    return ResponseHelper.format_response(response)


@router.get(
    "/trending",
    response_model=TrendingResponse,
    description="Retrieve a list of trending manga titles. These titles represent manga that are currently popular and generating significant attention among readers on MangaReader.",
)
async def trending():
    response = TrendingScraper().build()
    return ResponseHelper.format_response(response)


@router.get(
    "/manga/{slug}",
    response_model=MangaModel,
    description="""
        Retrieve detailed information about a specific manga based on its slug. This endpoint provides comprehensive data about the manga, including its title, author, genres, summary, and list of chapters.\\
        eg: `/api/v1/manga/one-piece-3/`
        - retrieve details about manga with **one-piece-3** as slug
    """,
)
async def manga(slug: str):
    response = MangaScraper(slug).build()
    return response


@router.get(
    "/search/{query}",
    response_model=SearchMangaResponse,
    description="Search for manga titles based on a query string. This endpoint allows users to find manga matching specific criteria, such as title, author, or genre. The search results provide relevant manga titles that closely match the provided query.",
)
async def search(query: str):
    response = SearchScraper(query).build()
    return ResponseHelper.format_response(response)
