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
        node_text = node.text(strip=True)
        return node_text.split(":")[1] if ":" in node_text else node_text

    def __get_item_int(self, property_name: str):
        item = self.__get_item(property_name)
        return float(item) if item else None

    def __get_item_list(self, property_name: str):
        nodes = self.parser.css(self.css_selectors.get(property_name, ""))
        return [node.text(strip=True) for node in nodes] if nodes else []

    def __get_item_attr(self, property_name: str, attr: str):
        node = self.parser.css_first(self.css_selectors.get(property_name, ""))
        return node.attributes[attr] if node else None

    def scrape(self):
        manga_dict = {
            "title": self.__get_item("title"),
            "alt_title": self.__get_item("alt_title"),
            "type": self.__get_item("type"),
            "genres": self.__get_item_list("genres"),
            "status": self.__get_item("status"),
            "score": self.__get_item_int("score"),
            "cover_src": self.__get_item_attr("cover_src", "src"),
            "synopsis": self.__get_item("synopsis"),
        }

        return manga_dict
