import re
from selectolax.parser import Node
from server.decorators import return_on_error
from server.helpers import HTMLHelper


class SearchParser:
    def __init__(self, query: str) -> None:
        self.query = query
        self.base_url = f"https://mangareader.to/search?keyword={query}"
        self.html_helper = HTMLHelper()
        self.parser = self.html_helper.get_parser(self.base_url)

    @return_on_error(None)
    def get_title(self, container: Node):
        node = container.css_first(".manga-name a")
        return node.text(strip=True)

    @return_on_error(None)
    def get_slug(self, container: Node):
        node = container.css_first(".manga-name a").attrs.get("href")
        return node.replace("/", "")

    @return_on_error("")
    def get_cover(self, container: Node):
        node = container.css_first(".manga-poster-img")
        return node.attributes.get("src")

    @return_on_error([])
    def get_genres(self, container: Node):
        node_list = container.css(".fd-infor .fdi-item a")
        return [node.text(strip=True) for node in node_list]

    @return_on_error([])
    def get_langs(self, container: Node):
        node = container.css_first(".tick-lang")
        return node.text(strip=True).split("/")

    @return_on_error(None)
    def get_chapters(self, container: Node):
        node = container.select("a").text_contains("Chap").matches[1]
        return float(re.findall(r"\d+", node.text(strip=True))[0])

    @return_on_error(None)
    def get_volumes(self, container: Node):
        node = container.select("a").text_contains("Vol").matches[1]
        return float(re.findall(r"\d+", node.text(strip=True))[0])

    def build_list(self):
        container_list = self.parser.css(".mls-wrap .item")
        manga_list = []

        for container in container_list:
            manga_list.append(
                {
                    "title": self.get_title(container),
                    "slug": self.get_slug(container),
                    "genres": self.get_genres(container),
                    "cover": self.get_cover(container),
                    "chapters": self.get_chapters(container),
                    "volumes": self.get_volumes(container),
                }
            )

        return manga_list
