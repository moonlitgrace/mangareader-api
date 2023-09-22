from selectolax.parser import Node
from ..utils import get_attribute, get_text
from ..helpers.html_helper import HTMLHelper


class PopularScraper:
    def __init__(self) -> None:
        url = "https://mangareader.to/home"
        # Facades
        self.html_helper = HTMLHelper()
        # Parser
        self.parser = self.html_helper.get_parser(url)

    @staticmethod
    def __get_slug(node: Node) -> str | None:
        slug = get_attribute(node, "a.link-mask", "href")
        return slug.replace("/", "") if slug else None

    @staticmethod
    def __get_langs(node: Node) -> list | None:
        langs = get_text(node, ".mp-desc p:nth-of-type(3)")
        return langs.split("/") if langs else None

    @staticmethod
    def __get_chapters_volumes(node: Node, index: int) -> dict | None:
        data = get_text(node, f".mp-desc p:nth-of-type({index})")
        if data:
            total = data.split()[1]
            lang = data.split()[2].translate(str.maketrans("", "", "[]"))

            data_dict = {"total": total, "lang": lang}

            return data_dict
        return None

    def __build_dict(self, node) -> dict:
        manga_dict = {
            "rank": get_text(node, ".number span"),
            "title": get_text(node, ".anime-name"),
            "slug": self.__get_slug(node),
            "cover": get_attribute(node, "img.manga-poster-img", "src"),
            "rating": get_text(node, ".mp-desc p:nth-of-type(2)"),
            "langs": self.__get_langs(node),
            "chapters": self.__get_chapters_volumes(node, 4),
            "volumes": self.__get_chapters_volumes(node, 5),
        }

        return manga_dict

    def scrape(self) -> list:
        mangas_list = []
        container = self.parser.css_first("div#manga-trending")
        nodes_list = container.css("div.swiper-slide")

        for index, node in enumerate(nodes_list, start=1):
            manga_dict = {"id": index, **self.__build_dict(node)}

            mangas_list.append(manga_dict)

        return mangas_list
