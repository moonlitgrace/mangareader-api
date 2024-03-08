from selectolax.parser import Node

from ...helpers.parser import HTMLParserHelper
from ..base_scraper import BaseScraper
from ...constants.endpoints import API_ENDPOINTS
from ...helpers.string import StringHelper
from ...decorators.return_on_error import return_on_error


class SearchScraper(BaseScraper):
    def __init__(self, query: str):
        super().__init__()

        endpoint = API_ENDPOINTS.get("search")
        sluggified_query = StringHelper.slugify(query, "+")
        url = f"{endpoint}?keyword={sluggified_query}"

        self.parser = HTMLParserHelper.get_parser(url)
        self.string_helper = StringHelper()

    def __get_title__(self, parent: Node):
        node = parent.css_first("h3.manga-name")
        return node.text(strip=True)

    def __get_genres__(self, parent: Node):
        genres = parent.css(".fdi-cate a")
        return [genre.text(strip=True).lower() for genre in genres]

    def __get_slug__(self, parent: Node):
        node = parent.css_first("h3.manga-name a")
        return node.attrs.get("href")[1:]

    def __get_cover__(self, parent: Node):
        node = parent.css_first("img.manga-poster-img")
        return node.attrs.get("src")

    def __get_chapters__(self, parent: Node):
        chap_str = parent.select("a").text_contains("Chap ").matches[0]
        return self.string_helper.clean(chap_str.text(strip=True).split(" ")[1])

    @return_on_error(0)
    def __get_volumes__(self, parent: Node):
        vol_str = parent.select("a").text_contains("Vol ").matches[0]
        return self.string_helper.clean(vol_str.text(strip=True).split(" ")[1])

    def __get_langs__(self, parent: Node):
        node = parent.css_first(".tick-lang")
        return node.text(strip=True).lower().split("/")

    def scrape(self):
        nodes = self.parser.css(".manga_list-sbs .mls-wrap .item")
        response_list = []

        for node in nodes:
            response_list.append(
                {
                    "title": self.__get_title__(node),
                    "slug": self.__get_slug__(node),
                    "genres": self.__get_genres__(node),
                    "langs": self.__get_langs__(node),
                    "cover": self.__get_cover__(node),
                    "chapters": self.__get_chapters__(node),
                    "volumes": self.__get_volumes__(node),
                }
            )

        return response_list
