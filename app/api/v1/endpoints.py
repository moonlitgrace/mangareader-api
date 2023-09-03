from dataclasses import astuple
from fastapi import APIRouter
from fastapi.responses import JSONResponse

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
async def get_popular():
	return PopularScraper().parse()

# get top 10 mangas list
@router.get("/top-10", response_model=list[TopTenMangaModel])
async def get_top_ten():
	return TopTenScraper().parse()

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

		return JSONResponse(
			content = {
				"detail": {
					"error": error,
					"message": message,
					"status_code": status_code
				}
			},
			status_code=status_code
		)

# get details about specific manga
@router.get("/manga/{slug}", response_model=MangaModel)
async def get_manga(slug: str):
	return MangaScraper(slug).parse()