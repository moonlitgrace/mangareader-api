from selectolax.parser import Node
from ..utils import get_text, get_attribute
from ..helpers.html_helper import HTMLHelper


class TopTenScraper:
    def __init__(self) -> None:
        url = "https://mangareader.to/home"
        # Facades
        self.html_helper = HTMLHelper()
        # Parser
        self.parser = self.html_helper.get_parser(url)

    def __get_slug(self, node: Node) -> str | None:
        slug = get_attribute(node, ".desi-head-title a", "href")
        return slug.replace("/", "") if slug else None

    def __get_chapters(self, node: Node) -> dict | None:
        chapters_string = get_text(node, ".desi-sub-text")
        if chapters_string:
            total = chapters_string.split()[1]
            lang = chapters_string.split()[2].translate(str.maketrans("", "", "[]"))

            data_dict = {"total": total, "lang": lang}

            return data_dict
        return None

    def __get_genres(self, node: Node) -> list | None:
        genres = node.css(".sc-detail .scd-genres span")
        return [genre.text() for genre in genres] if genres else None

    def __build_dict(self, node: Node) -> dict:
        manga_dict = {
            "title": get_text(node, ".desi-head-title a"),
            "slug": self.__get_slug(node),
            "cover": get_attribute(node, "img.manga-poster-img", "src"),
            "synopsis": get_text(node, ".sc-detail .scd-item"),
            "chapters": self.__get_chapters(node),
            "genres": self.__get_genres(node),
        }

        return manga_dict

    def scrape(self) -> list:
        managas_list = []
        container = self.parser.css_first(".deslide-wrap #slider .swiper-wrapper")
        node_list = container.css("div.swiper-slide")

        for index, node in enumerate(node_list, start=1):
            manga_dict = {"id": index, **self.__build_dict(node)}

            managas_list.append(manga_dict)
        return managas_list
