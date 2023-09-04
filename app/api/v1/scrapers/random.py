import requests
from selectolax.parser import HTMLParser, Node
from ..utils import get_attribute, get_text
# manga scraper
from .manga import MangaScraper

class RandomScraper:
    def __init__(self):
        # get parser
        self.parser = self.__get_parser()

    @staticmethod
    def __get_parser():
        url = "https://mangareader.to/random/"
        res = requests.get(url)
        return HTMLParser(res.content)

    def __get_slug(self, node: Node):
        slug_string = get_attribute(node, "#ani_detail .ani_detail-stage .anis-content .anisc-detail .manga-buttons a", "href")
        return slug_string.split("/")[-1] if slug_string else None

    def __get_genres(self, node: Node):
        genres = node.css(".anisc-detail .sort-desc .genres a")
        return [genre.text() for genre in genres] if genres else None

    def __get_authers(self, node: Node):
        authers = node.css(".anisc-detail .anisc-info .item:nth-child(3) a")
        return [auther.text() for auther in authers] if authers else None

    def __get_magazines(self, node: Node):
        magazines = node.css(".anisc-detail .anisc-info .item:nth-child(4) a")
        return [magazine.text() for magazine in magazines] if magazines else None

    def __get_published(self, node: Node):
        published_string = get_text(node, ".anisc-detail .anisc-info .item:nth-child(5) .name")
        if published_string:
            date = published_string.split(" to ")[0]
            return date
        return None

    def __get_views(self, node: Node):
        views_string = get_text(node, ".anisc-detail .anisc-info .item:nth-child(7) .name")
        return views_string.replace(",", "") if views_string else None

    def __get_chapters_volumes(self, type: str):
        items = self.parser.css(f"#main-content #list-{type} .dropdown-menu a")

        item_list = []
        for item in items:
            text = item.text().translate(str.maketrans("", "", "[]()"))

            item_dict = {
                "total": text.split()[2],
                "lang": text.split()[0]
            }

            item_list.append(item_dict)
        return item_list

    def parse(self):
        node = self.parser.css_first("#ani_detail")
        manga_dict = {
            "id": self.__get_slug(node),
            "title": get_text(node, ".anisc-detail .manga-name"),
            "alt_title": get_text(node, ".anisc-detail .manga-name-or"),
            "slug": self.__get_slug(node),
            "type": get_text(node, ".anisc-detail .anisc-info .item:nth-child(1) a"),
            "status": get_text(node, ".anisc-detail .anisc-info .item:nth-child(2) .name"),
            "published": self.__get_published(node),
            "score": get_text(node, ".anisc-detail .anisc-info .item:nth-child(6) .name"),
            "views": self.__get_views(node),
            "cover": get_attribute(node, ".anisc-poster .manga-poster-img", "src"),
            "synopsis": get_text(node, ".anisc-detail .sort-desc .description"),
            "genres": self.__get_genres(node),
            "authers": self.__get_authers(node),
            "mangazines": self.__get_magazines(node),
            "chapters": self.__get_chapters_volumes("chapter"),
            "volumes": self.__get_chapters_volumes("vol")
        }

        return manga_dict