from ..helpers import HTMLParserHelper
from app.helpers import StringHelper
from ..constants import API_ENDPOINTS


class MangaScraper:
    def __init__(self, slug: str):
        self.slug = slug
        endpoint = API_ENDPOINTS.get("manga")
        url = f"{endpoint}/{slug}"

        self.parser = HTMLParserHelper.get_parser(url)
        self.string_helper = StringHelper()

    @property
    def __get_title__(self):
        node = self.parser.css_first("h2.manga-name")
        return node.text(strip=True)

    @property
    def __get_alt_title__(self):
        node = self.parser.css_first("div.manga-name-or")
        return node.text(strip=True)

    @property
    def __get_genres__(self):
        genres = self.parser.css(".genres a")
        return [genre.text(strip=True).lower() for genre in genres]

    @property
    def __get_cover__(self):
        node = self.parser.css_first(".manga-poster-img")
        return node.attrs.get("src")

    @property
    def __get_synopsis__(self):
        node = self.parser.css_first(".description")
        return node.text(strip=True)

    @property
    def __get_type__(self):
        node = self.parser.select("div.item.item-title").text_contains("Type:").matches[0]
        return node.text(strip=True).split(":")[1].lower()

    @property
    def __get_rating__(self):
        node = self.parser.select("div.item.item-title").text_contains("Score:").matches[0]
        return node.text(strip=True).split(":")[1].lower()

    @property
    def __get_authors__(self):
        node = (
            self.parser.select("div.item.item-title").text_contains("Authors:").matches[0]
        )
        return node.text(strip=True).split(":")[1].split("(")[0]

    @property
    def __get_published_date__(self):
        node = (
            self.parser.select("div.item.item-title").text_contains("Published:").matches[0]
        )
        return self.string_helper.clean(node.text(strip=True).split(":")[1].split("to")[0])

    def build(self):
        return {
            "title": self.__get_title__,
            "slug": self.slug,
            "alt_title": self.__get_alt_title__,
            "genres": self.__get_genres__,
            "type": self.__get_type__,
            "rating": self.__get_rating__,
            "authors": self.__get_authors__,
            "published_date": self.__get_published_date__,
            "cover": self.__get_cover__,
            "synopsis": self.__get_synopsis__,
        }
