from fastapi import APIRouter, HTTPException
from providers import providers_urls, providers_css_selectors
from .scrapers import MangaScraper

router = APIRouter()


@router.get(path="/{provider}/manga/{id}/{title}")
async def manga(provider: str, id: int, title: str):
    provider_url = providers_urls.get(provider)
    if not provider_url:
        raise HTTPException(404, detail="Provider not found!")

    manga_url = f"{provider_url}/{id}/{title}/"
    css_selectors = providers_css_selectors.get(provider).get("manga")

    manga_scraper = MangaScraper(url=manga_url, css_selectors=css_selectors)
    return manga_scraper.scrape()
