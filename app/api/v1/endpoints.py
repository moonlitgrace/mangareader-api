from dataclasses import astuple
from fastapi import APIRouter, HTTPException, Query
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
@handle_exceptions("Something went wrong, please try again!", 503)
async def get_popular(offset: int = 0, limit: int = Query(10, lt=10)):
	response = PopularScraper().parse()
	return response[offset: offset+limit]

# get top 10 mangas list
@router.get("/top-10", response_model=list[TopTenMangaModel])
@handle_exceptions("Something went wrong, please try again!", 503)
async def get_top_ten(offset: int = 0, limit: int = Query(10, lt=10)):
	response = TopTenScraper().parse()
	return response[offset: offset+limit]

# get most viewed mangas list by chart (dynamic)
@router.get("/most-viewed/{chart}", response_model=list[MostViewedMangaModel])
@handle_exceptions("Something went wrong, please try again!", 503)
async def get_most_viewed(chart: str):
	most_viewed_scraper = MostViewedScraper()

	if chart in most_viewed_scraper.CHARTS:
		return most_viewed_scraper.parse(chart)
	else:
		message = f"Passed query ({chart}) is invalid. Valid queries {' | '.join(most_viewed_scraper.CHARTS)}"
		status_code = 400

		raise HTTPException(
			detail = {
				"message": message,
				"status_code": status_code
			},
			status_code=status_code
		)

# get details about specific manga
@router.get("/manga/{slug}", response_model=MangaModel)
@handle_exceptions("Manga not found, try another!", 404)
async def get_manga(slug: str):
	response = MangaScraper(slug).parse()
	return response

# search mangas
@router.get("/search")
async def search(keyword: str):
	return keyword.replace(" ", "+")