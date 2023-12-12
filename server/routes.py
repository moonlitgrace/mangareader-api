from fastapi import APIRouter
from providers import providers_urls, providers_css_selectors

router = APIRouter()


@router.get(path="/{provider}/manga/{id}/{title}")
async def manga(provider: str, id: int, title: str):
    provider_url = providers_urls.get(provider)
    manga_url = f"{provider_url}/{id}/{title}/"
    css_selectors = providers_css_selectors.get(provider).get("manga")
    return css_selectors
