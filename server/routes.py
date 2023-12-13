from fastapi import APIRouter, HTTPException
from providers import providers_urls, providers_css_selectors
from .scrapers import MangaScraper, SearchMangaScraper
from .models import Manga

router = APIRouter()


@router.get(path="/{provider}/manga/{title}", response_model=Manga)
async def manga(provider: str, title: str) -> Manga:
    provider_url = providers_urls.get(provider)
    if not provider_url:
        raise HTTPException(404, detail="Provider not found!")

    provider_manga_url = provider_url.get("manga")
    manga_url = f"{provider_manga_url}{title}/"
    css_selectors = providers_css_selectors.get(provider).get("manga")

    manga_scraper = MangaScraper(url=manga_url, css_selectors=css_selectors)
    return manga_scraper.scrape()


@router.get(path="/{provider}/search/{query}")
async def search(provider: str, query: str):
    provider_url = providers_urls.get(provider)
    if not provider_url:
        raise HTTPException(404, detail="Provider not found!")

    provider_search_url = provider_url.get("search")
    search_url = f"{provider_search_url}{query}"
    css_selectors = providers_css_selectors.get(provider).get("search")

    search_scraper = SearchMangaScraper(url=search_url, css_selectors=css_selectors)
    return search_scraper.scrape()
