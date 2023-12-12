from typing import Dict, Type
from . import mangareader


class MangaReader:
    manga = mangareader.manga


providers_urls: Dict = {
    "mangareader": "https://mangareader.to",
}

providers_css_selectors: Dict[str, Dict[str, Type[MangaReader]]] = {
    "mangareader": {
        "manga": MangaReader.manga,
    },
}
