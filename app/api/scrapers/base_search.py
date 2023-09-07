import requests
from selectolax.parser import HTMLParser, Node
from ..decorators.return_decorator import return_on_error


class BaseSearchScraper:
    def __init__(self, url: str):
        self.url = url
        self.parser = self.__get_parser()

    def __get_parser(self):
        res = requests.get(self.url)
        return HTMLParser(res.content)

    def get_manga_id(self, node: Node):
        id = self.get_slug(node)
        return int(id.split("-")[-1]) if id else 0

    @staticmethod
    @return_on_error("")
    def get_cover(node: Node):
        image_node = node.css_first(".manga-poster img")
        src = image_node.attributes["src"]
        return src if src else ""

    @staticmethod
    @return_on_error("")
    def get_manga_title(node: Node):
        title_node = node.css_first(".manga-detail .manga-name a")
        return title_node.text(strip=True)

    @staticmethod
    @return_on_error("")
    def get_slug(node: Node):
        slug_node = node.css_first(".manga-detail .manga-name a")
        slug = slug_node.attributes["href"]
        return slug.replace("/", "") if slug else ""

    @staticmethod
    @return_on_error([])
    def get_langs(node: Node):
        langs_string = node.css_first(".manga-poster .tick-lang").text(strip=True)
        return langs_string.split("/") if langs_string else []

    @staticmethod
    @return_on_error([])
    def get_genres(node: Node):
        genres = node.css(".manga-detail .fd-infor a")
        return [genre.text() for genre in genres] if genres else []

    @staticmethod
    @return_on_error({})
    def get_chapters(node: Node):
        chapters_node = node.css_first(".manga-detail .fd-list:nth-child(1) .chapter a")
        if chapters_node:
            chapters = chapters_node.text(strip=True)
            total = chapters.split()[1]
            lang = chapters.split()[2].translate(str.maketrans("", "", "[]"))

            chapters = {"total": total, "lang": lang}

            return chapters
        return {}

    @return_on_error([])
    def scrape(self) -> list:
        manga_list = []
        container = self.parser.css_first(".manga_list-sbs")
        node_list = container.css("div.item.item-spc")

        for index, node in enumerate(node_list, start=1):
            manga_dict = {
                "id": index,
                "manga_id": self.get_manga_id(node),
                "title": self.get_manga_title(node),
                "slug": self.get_slug(node),
                "cover": self.get_cover(node),
                "langs": self.get_langs(node),
                "genres": self.get_genres(node),
                "chapters": self.get_chapters(node),
            }

            manga_list.append(manga_dict)
        return manga_list
