from typing import Dict, Type
from . import mangareader
from server.models import Manga


class BaseProvider:
    manga: Type[Manga]


class MangaReaderProvider(BaseProvider):
    manga = mangareader.manga


providers_urls: Dict = {
    "mangareader": "https://mangareader.to",
}

providers_css_selectors: Dict[str, Dict[str, Type[BaseProvider]]] = {
    "mangareader": {
        "manga": MangaReaderProvider.manga,
    },
}
