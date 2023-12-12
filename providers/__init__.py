from typing import Dict, Type
from . import myanimelist, mangareader


class MangaReader:
    manga = mangareader.manga


class MyAnimeList:
    manga = myanimelist.manga


providers_urls: Dict = {
    "myanimelist": "https://myanimelist.net/manga",
    "mangareader": "https://mangareader.to",
}

providers_css_selectors: Dict[str, Dict[str, Type[MyAnimeList]]] = {
    "mangareader": {
        "manga": MangaReader.manga,
    },
    "myanimelist": {
        "manga": MyAnimeList.manga,
    },
}
