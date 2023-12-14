from typing import Dict, Type
from . import mangareader
from server.models import Manga


class BaseProvider:
    manga: Type[Manga]


class MangaReaderProvider(BaseProvider):
    manga = mangareader.manga
    search = mangareader.search


providers_urls: Dict[str, Dict[str, str]] = {
    "mangareader": {
        "manga": "https://mangareader.to/",
        "search": "https://mangareader.to/search?keyword=",
    },
}

providers_css_selectors: Dict[str, Dict[str, Type[BaseProvider]]] = {
    "mangareader": {
        "manga": MangaReaderProvider.manga,
        "search": MangaReaderProvider.search,
    },
}
