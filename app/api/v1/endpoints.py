from fastapi import APIRouter, HTTPException, Query

from .utils import slugify

# scrapers
from .scrapers.popular import PopularScraper
from .scrapers.topten import TopTenScraper
from .scrapers.most_viewed import MostViewedScraper
from .scrapers.base_search import BaseSearchScraper
from .scrapers.base_manga import BaseMangaScraper

# models
from .models import (
    PopularMangaModel,
    TopTenMangaModel,
    MostViewedMangaModel,
    MangaModel,
    BaseSearchModel,
)

# router
router = APIRouter()


@router.get(
    "/popular",
    response_model=list[PopularMangaModel],
    summary="Popular Mangas",
    description="Get a list of Mangas which is popular/trending this season. Returns basic details of mangas, use its `slug` to get more details of Manga.",
)
async def get_popular(offset: int = 0, limit: int = Query(10, le=10)):
    response = PopularScraper().scrape()
    return response[offset : offset + limit]


@router.get(
    "/top-10",
    response_model=list[TopTenMangaModel],
    summary="Top 10 Mangas",
    description="Get a list of Mangas which is top 10 this season. Returns basic details of mangas, use its `slug` to get more details of Manga.",
)
async def get_top_ten(offset: int = 0, limit: int = Query(10, le=10)):
    response = TopTenScraper().scrape()
    return response[offset : offset + limit]


@router.get(
    "/most-viewed/{chart}",
    response_model=list[MostViewedMangaModel],
    summary="Most Viewed Mangas",
    description="Get a list of Mangas which is most viewed by chart - `today` `week` `month`. Returns basic details of mangas, use its `slug` to get more details of Manga.",
)
async def get_most_viewed(chart: str, offset: int = 0, limit: int = Query(10, le=10)):
    most_viewed_scraper = MostViewedScraper()

    if chart in most_viewed_scraper.CHARTS:
        response = most_viewed_scraper.scrape(chart)
        return response[offset : offset + limit]
    else:
        message = f"Passed query ({chart}) is invalid. Valid queries {' | '.join(most_viewed_scraper.CHARTS)}"
        status_code = 400

        raise HTTPException(
            detail={"message": message, "status_code": status_code},
            status_code=status_code,
        )


@router.get(
    "/manga/{slug}",
    response_model=MangaModel,
    summary="Manga",
    description="Get more details about a specific Manga by `slug`, eg: `/manga/one-piece-3/` - returns the full details of that specific Manga.",
)
async def get_manga(slug: str):
    response = BaseMangaScraper(url=f"https://mangareader.to/{slug}").build_dict()
    return response


@router.get(
    "/search",
    response_model=list[BaseSearchModel],
    summary="Search Mangas",
    description="Search Mangas with a `keyword` as query. eg: `/search/?keyword=one piece/` - returns a list of Mangas according to this keyword.",
)
async def search(
    keyword: str, page: int = 1, offset: int = 0, limit: int = Query(10, le=18)
):
    url = f"https://mangareader.to/search?keyword={keyword}&page={page}"
    response = BaseSearchScraper(url).scrape()
    return response[offset : offset + limit]


@router.get(
    "/random",
    response_model=MangaModel,
    summary="Random",
    description="Get details about random Manga. Returns a `dict` of randomly picked Manga. Note: some fields might be `null` because all animes are not registered properly in database.",
)
async def random():
    response = BaseMangaScraper(url="https://mangareader.to/random/").build_dict()
    return response


@router.get(
    "/completed",
    response_model=list[BaseSearchModel],
    summary="Completed Mangas",
    description="Get list of completed airing Mangas. eg: `/completed/` - returns a list of Mangas which is completed airing lately. Also has `sort` query which get each pages of Mangas ( 1 page contains 18 Mangas ): valid `sort` queries - `default` `last-updated` `score` `name-az` `release-date` `most-viewed`.",
)
async def completed(
    page: int = 1, sort: str = "default", offset: int = 0, limit: int = Query(10, le=18)
):
    slugified_sort = slugify(sort, "-")
    url = f"https://mangareader.to/completed/?sort={slugified_sort}&page={page}"
    response = BaseSearchScraper(url).scrape()
    return response[offset : offset + limit]


@router.get(
    "/genre/{genre}",
    response_model=list[BaseSearchModel],
    summary="Genre",
    description="Search Mangas with genres. eg: `/genre/action/` - returns a list of Mangas with genre `action`. Also has `sort` query which get each pages of Mangas ( 1 page contains 18 Mangas ): valid `sort` queries - `default` `last-updated` `score` `name-az` `release-date` `most-viewed`.",
)
async def genre(
    genre: str,
    page: int = 1,
    sort: str = "default",
    offset: int = 0,
    limit: int = Query(10, le=18),
):
    slugified_sort = slugify(sort, "-")
    url = f"https://mangareader.to/genre/{genre}/?sort={slugified_sort}&page={page}"
    response = BaseSearchScraper(url).scrape()
    return response[offset : offset + limit]
