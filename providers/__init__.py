from typing import Dict, Type
from . import myanimelist


class MyAnimeList:
    manga = myanimelist.manga


providers_urls: Dict = {
    "myanimelist": "https://myanimelist.net/manga",
    "mangareader": "https://mangareader.to",
}

providers_css_selectors: Dict[str, Dict[str, Type[MyAnimeList]]] = {
    "myanimelist": {
        "manga": MyAnimeList.manga,
    }
}
