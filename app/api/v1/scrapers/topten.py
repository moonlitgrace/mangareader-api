from fastapi.responses import JSONResponse
from selectolax.parser import HTMLParser, Node
import requests

class TopTenScraper():
    def __init__(self):
        super().__init__()

        # get parser
        self.parser = self.__get_parser()
    
    @staticmethod
    def __get_parser():
        url = "https://mangareader.to/home"
        res = requests.get(url)

        return HTMLParser(res.content)

    @staticmethod
    def __get_text(node: Node, selector: str):
        element = node.css_first(selector)
        return element.text() if element else None

    @staticmethod
    def __get_attribute(node: Node, selector: str, attribute: str):
        element = node.css_first(selector)
        return element.attributes[attribute] if element else None

    def __get_slug(self, node: Node):
        slug = self.__get_attribute(node, ".desi-head-title a", "href")
        return slug.replace("/", "") if slug else None

    def __get_chapters(self, node: Node):
        chapters_string = self.__get_text(node, ".desi-sub-text")
        if chapters_string:
            total = chapters_string.split()[1]
            lang = chapters_string.split()[2].translate(str.maketrans("", "", "[]"))

            data_dict = {
                "total": total,
                "lang": lang
            }

            return data_dict
        return None

    def __get_genres(self, node: Node):
        genres = node.css(".sc-detail .scd-genres span")
        return [genre.text() for genre in genres] if genres else None

    def __build_dict(self, node: Node):
        manga_dict = {
            "title": self.__get_text(node, ".desi-head-title a"),
            "slug": self.__get_slug(node),
            "cover": self.__get_attribute(node, "img.manga-poster-img", "src"),
            "synopsis": self.__get_text(node, ".sc-detail .scd-item"),
            "chapters": self.__get_chapters(node),
            "genres": self.__get_genres(node)
        }

        return manga_dict

    def parse(self):
        try:
            managas_list = []

            container = self.parser.css_first(".deslide-wrap #slider .swiper-wrapper")
            node_list = container.css("div.swiper-slide")

            for index, node in enumerate(node_list, start=1):
                manga_dict = {
                    "id": index,
                    **self.__build_dict(node)
                }

                managas_list.append(manga_dict)
            return managas_list
        except Exception as e:
            error = "Couldn't connect to website"
            message = "Something went wrong while trying to scrape, please try again later!"
            status_code = 503

            return JSONResponse(
                content = {
                    "detail": {
                        "error": error,
                        "message": message,
                        "status_code": status_code
                    }
                },
                status_code=status_code
            )