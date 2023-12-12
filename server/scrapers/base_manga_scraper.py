from typing import Dict
from server.helpers import ScrapeHelper, HTMLHelper


class BaseMangaScraper:
    def __init__(self, url: str, css_selectors: Dict) -> None:
        # facades
        self.string_helper = ScrapeHelper()
        self.html_helper = HTMLHelper()
        self.parser = self.html_helper.get_parser(url)
