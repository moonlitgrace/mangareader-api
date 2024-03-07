from selectolax.parser import Node

from ...helpers.parser import HTMLParserHelper
from ...constants.endpoints import API_ENDPOINTS
from ..base_scraper import BaseScraper
from ...helpers.string import StringHelper

class TrendingScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        url = API_ENDPOINTS.get("home")

        self.parser = HTMLParserHelper.get_parser(url)
        self.string_helper = StringHelper()

    def __get_title__(self, parent: Node):
        node = parent.css_first(".anime-name")
        return node.text(strip=True)

    def __get_slug__(self, parent: Node):
        node = parent.css_first(".manga-poster .link-mask")
        slug = node.attrs.get("href")
        return slug[1:]

    def __get_cover__(self, parent: Node):
        node = parent.css_first(".manga-poster-img")
        return node.attrs.get("src")

    def __get_chapters__(self, parent: Node):
        node = parent.select("strong").text_contains("Chap").matches[0]
        chapters = node.text(strip=True).split(" ")[1]
        return self.string_helper.clean(chapters)

    def __get_volumes__(self, parent: Node):
        node = parent.select("strong").text_contains("Vol").matches[0]
        volumes = node.text(strip=True).split(" ")[1]
        return self.string_helper.clean(volumes)

    def __get_rating__(self, parent: Node):
        node = parent.css_first(".mp-desc p:nth-child(2)")
        return node.text(strip=True)

    def __get_langs__(self, parent: Node):
        node = parent.css_first(".mp-desc p:nth-child(3)")
        return node.text(strip=True).split("/")

    def scrape(self):
        nodes = self.parser.css("#trending-home .swiper-wrapper .swiper-slide")
        response_list = []

        for node in nodes:
            response_list.append({
                "title": self.__get_title__(node),
                "slug": self.__get_slug__(node),
                "cover": self.__get_cover__(node),
                "rating": self.__get_rating__(node),
                "langs": self.__get_langs__(node),
                "chapters": self.__get_chapters__(node),
                "volumes": self.__get_volumes__(node),
            })

        return response_list