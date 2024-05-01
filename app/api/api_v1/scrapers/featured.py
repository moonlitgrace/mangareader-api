from selectolax.parser import Node

from ..helpers import HTMLParserHelper
from ..constants import API_ENDPOINTS
from app.helpers import StringHelper


class FeaturedScraper():
    def __init__(self):
        super().__init__()
        url = API_ENDPOINTS["home"]

        self.parser = HTMLParserHelper.get_parser(url)
        self.string_helper = StringHelper()

    def __get_title__(self, parent: Node):
        node = parent.css_first(".desi-head-title a")
        return node.text(strip=True)

    def __get_slug__(self, parent: Node):
        node = parent.css_first("a.manga-poster")
        slug = node.attrs.get("href")
        return slug[1:]

    def __get_genres__(self, parent: Node):
        genres = parent.css(".scd-genres span")
        return [genre.text(strip=True).lower() for genre in genres]

    def __get_cover__(self, parent: Node):
        node = parent.css_first("img.manga-poster-img")
        return node.attrs.get("src")

    def __get_synopsis__(self, parent: Node):
        node = parent.css_first(".sc-detail .scd-item")
        return node.text(strip=True)

    def __get_chaper__(self, parent: Node):
        node = parent.css_first(".desi-sub-text")
        chapter = node.text(strip=True).split(" ")[1]
        return self.string_helper.clean(chapter)

    def build(self):
        nodes = self.parser.css("#slider .swiper-wrapper .swiper-slide")
        response_list = []

        for node in nodes:
            response_list.append(
                {
                    "title": self.__get_title__(node),
                    "slug": self.__get_slug__(node),
                    "genres": self.__get_genres__(node),
                    "cover": self.__get_cover__(node),
                    "synopsis": self.__get_synopsis__(node),
                    "chapter": self.__get_chaper__(node),
                }
            )

        return response_list
