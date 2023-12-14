from typing import List
from fastapi import APIRouter, HTTPException
from providers import providers_urls, providers_css_selectors
from .scrapers import MangaScraper, SearchMangaScraper
from .models import Manga, Search

router = APIRouter()


@router.get(path="/services")
async def services():
    providers_list = {
        provider: list(providers_css_selectors[provider])
        for provider in providers_css_selectors
    }
    return providers_list


@router.get(path="/{provider}/manga/{query}", response_model=Manga)
async def manga(provider: str, query: str) -> Manga:
    provider_url = providers_urls.get(provider)
    if not provider_url:
        raise HTTPException(404, detail="Provider not found!")

    provider_manga_url = provider_url.get("manga")
    if not provider_manga_url:
        raise HTTPException(404, detail=f"{provider} does't provide 'manga' service")

    manga_url = f"{provider_manga_url}{query}/"
    css_selectors = providers_css_selectors.get(provider).get("manga")

    manga_scraper = MangaScraper(url=manga_url, css_selectors=css_selectors)
    return manga_scraper.scrape()


@router.get(path="/{provider}/search/{query}", response_model=List[Search])
async def search(provider: str, query: str):
    provider_url = providers_urls.get(provider)
    if not provider_url:
        raise HTTPException(404, detail="Provider not found!")

    provider_search_url = provider_url.get("search")
    if not provider_search_url:
        raise HTTPException(404, detail=f"{provider} does't provide 'search' service")

    search_url = f"{provider_search_url}{query}"
    css_selectors = providers_css_selectors.get(provider).get("search")

    search_scraper = SearchMangaScraper(url=search_url, css_selectors=css_selectors)
    return search_scraper.scrape()
