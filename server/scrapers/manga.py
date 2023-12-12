from typing import Dict
from server.helpers import ScrapeHelper, HTMLHelper


class MangaScraper:
    def __init__(self, url: str, css_selectors: Dict) -> None:
        # facades
        self.string_helper = ScrapeHelper()
        self.html_helper = HTMLHelper()
        self.parser = self.html_helper.get_parser(url)
        self.css_selectors = css_selectors

    def __get_item(self, property_name: str):
        node = self.parser.css_first(self.css_selectors.get(property_name, ""))
        return node.text(strip=True) if node else None

    def scrape(self):
        manga_dict = {"title": self.__get_item("title")}

        return manga_dict
