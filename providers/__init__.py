from typing import Dict
from . import myanimelist

providers_urls: Dict = {
    "myanimelist": "https://myanimelist.net/manga",
    "mangareader": "https://mangareader.to",
}

providers_css_selectors = {
    "myanimelist": {
        "manga": myanimelist.manga,
    }
}
