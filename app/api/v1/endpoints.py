from dataclasses import astuple
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

# decorators
from .decorators import handle_exceptions
# scrapers
from .scrapers.popular import PopularScraper
from .scrapers.topten import TopTenScraper
from .scrapers.most_viewed import MostViewedScraper
from .scrapers.manga import MangaScraper
# models
from .models import (
	PopularMangaModel,
	BaseModel,
	TopTenMangaModel,
	MostViewedMangaModel,
	MangaModel
)

# router
router = APIRouter()

# get popular/trending mangas list
@router.get("/popular", response_model=list[PopularMangaModel])
@handle_exceptions("Something went wrong, please try again later!", 503)
async def get_popular(skip: int = 0, limit: int = 10):
	response = PopularScraper().parse()
	return response[skip: skip+limit]

# get top 10 mangas list
@router.get("/top-10", response_model=list[TopTenMangaModel])
@handle_exceptions("Something went wrong, please try again later!", 503)
async def get_top_ten(skip: int = 0, limit: int = 10):
	response = TopTenScraper().parse()
	return response[skip: skip+limit]

# get most viewed mangas list by chart (dynamic)
@router.get("/most-viewed/{chart}", response_model=list[MostViewedMangaModel])
async def get_most_viewed(chart: str):
	most_viewed_scraper = MostViewedScraper()

	if chart in most_viewed_scraper.CHARTS:
		return most_viewed_scraper.parse(chart)
	else:
		error = f"{chart} not in {', '.join(most_viewed_scraper.CHARTS)}"
		message = f"Passed query ({chart}) is invalid. Valid queries {' | '.join(most_viewed_scraper.CHARTS)}"
		status_code = 400

		raise HTTPException(
			detail = {
				"error": error,
				"message": message,
				"status_code": status_code
			},
			status_code=status_code
		)

# get details about specific manga
@router.get("/manga/{slug}", response_model=MangaModel)
@handle_exceptions("Manga not found!", 404)
async def get_manga(slug: str):
	response = MangaScraper(slug).parse()
	return response