from typing import Dict
from selectolax.parser import Node
from ..helpers import HTMLHelper, StringHelper


class SearchMangaScraper:
    def __init__(self, url: str, css_selectors: Dict) -> None:
        # facades
        self.html_helper = HTMLHelper()
        self.string_helper = StringHelper()
        self.css_selectors = css_selectors
        self.parser = self.html_helper.get_parser(url)

    def __get_item(self, node_main: Node, property_name: str):
        node = node_main.css_first(self.css_selectors.get(property_name, ""))
        node_text = node.text(strip=True)
        return node_text.split(":")[1] if ":" in node_text else node_text

    def __get_item_int(self, node_main: Node, property_name: str):
        item = self.__get_item(node_main, property_name)
        return float(item) if item else None

    def __get_item_list(self, node_main: Node, property_name: str):
        nodes = node_main.css(self.css_selectors.get(property_name, ""))
        return [node.text(strip=True) for node in nodes] if nodes else []

    def __get_item_attr(self, property_name: str, attr: str):
        node = self.parser.css_first(self.css_selectors.get(property_name, ""))
        return node.attributes[attr] if node else None

    def scrape(self):
        mangas_list = []

        nodes = self.parser.css(self.css_selectors.get("nodes_wrapper"))
        for node in nodes:
            manga_dict = {
                "title": self.__get_item(node, "title"),
            }

            mangas_list.append(manga_dict)
        return mangas_list
