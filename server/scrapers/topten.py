from selectolax.parser import Node

from ..decorators.return_decorator import return_on_error
from ..helpers.scraper import ScrapeHelper
from ..helpers.html_helper import HTMLHelper


class TopTenScraper:
    def __init__(self) -> None:
        url = "https://mangareader.to/home"
        # Facades
        self.html_helper = HTMLHelper()
        self.scraper_helper = ScrapeHelper()
        # Parser
        self.parser = self.html_helper.get_parser(url)

    @return_on_error("")
    def __get_slug(self, node: Node) -> str:
        slug = self.scraper_helper.get_attribute(node, ".desi-head-title a", "href")
        return slug.replace("/", "") if slug else ""

    @return_on_error({})
    def __get_chapters(self, node: Node):
        chapters_string = self.scraper_helper.get_text(node, ".desi-sub-text")
        if chapters_string:
            total = chapters_string.split()[1]
            lang = chapters_string.split()[2].translate(str.maketrans("", "", "[]"))

            data_dict = {"total": total, "lang": lang}

            return data_dict
        return {}

    @staticmethod
    @return_on_error([])
    def __get_genres(node: Node):
        genres = node.css(".sc-detail .scd-genres span")
        return [genre.text() for genre in genres] if genres else []

    @return_on_error({})
    def __build_dict(self, node: Node):
        manga_dict = {
            "title": self.scraper_helper.get_text(node, ".desi-head-title a"),
            "slug": self.__get_slug(node),
            "cover": self.scraper_helper.get_attribute(node, "img.manga-poster-img", "src"),
            "synopsis": self.scraper_helper.get_text(node, ".sc-detail .scd-item"),
            "chapters": self.__get_chapters(node),
            "genres": self.__get_genres(node),
        }

        return manga_dict

    @property
    @return_on_error([])
    def scrape(self):
        managas_list = []
        container = self.parser.css_first(".deslide-wrap #slider .swiper-wrapper")
        node_list = container.css("div.swiper-slide")

        for index, node in enumerate(node_list, start=1):
            manga_dict = {"id": index, **self.__build_dict(node)}

            managas_list.append(manga_dict)
        return managas_list
