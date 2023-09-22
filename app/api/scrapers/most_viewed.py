from selectolax.parser import Node
from ..utils import get_text, get_attribute
from ..helpers.html_helper import HTMLHelper


class MostViewedScraper:
    # Charts
    # eg. "today" | "week" | "month"
    CHARTS = ["today", "week", "month"]

    def __init__(self) -> None:
        url = "https://mangareader.to/home"
        # Facades
        self.html_helper = HTMLHelper()
        # Parser
        self.parser = self.html_helper.get_parser(url)

    def __get_slug(self, node: Node) -> str | None:
        slug = get_attribute(node, ".manga-detail .manga-name a", "href")
        return slug.replace("/", "") if slug else None

    def __get_cover(self, node: Node) -> str | None:
        cover = get_attribute(node, "img.manga-poster-img", "src")
        return cover.replace("200x300", "500x800") if cover else None

    def __get_views(self, node: Node) -> str | None:
        views_string = get_text(node, ".fd-infor .fdi-view")
        return views_string.split()[0].replace(",", "") if views_string else None

    def __get_langs(self, node: Node) -> list | None:
        langs_string = get_text(node, ".fd-infor > span:nth-child(1)")
        return [lang for lang in langs_string.split("/")] if langs_string else None

    def __get_chapters_volumes(self, node: Node, index: int) -> str | None:
        data_string = get_text(node, f".d-block span:nth-child({index})")
        return data_string.split()[1] if data_string else None

    def __get_genres(self, node: Node) -> list | None:
        genres = node.css(".fd-infor .fdi-cate a")
        return [genre.text() for genre in genres] if genres else None

    def __build_dict(self, node: Node) -> dict:
        manga_dict = {
            "rank": get_text(node, ".ranking-number span"),
            "title": get_text(node, ".manga-detail .manga-name a"),
            "slug": self.__get_slug(node),
            "cover": self.__get_cover(node),
            "views": self.__get_views(node),
            "langs": self.__get_langs(node),
            "chapters": self.__get_chapters_volumes(node, 1),
            "volumes": self.__get_chapters_volumes(node, 2),
            "genres": self.__get_genres(node),
        }

        return manga_dict

    def scrape(self, chart) -> list:
        mangas_list = []
        container = self.parser.css_first(f"#main-sidebar #chart-{chart}")
        node_list = container.css("ul > li")

        for index, node in enumerate(node_list, start=1):
            manga_dict = {"id": index, **self.__build_dict(node)}

            mangas_list.append(manga_dict)
        return mangas_list
