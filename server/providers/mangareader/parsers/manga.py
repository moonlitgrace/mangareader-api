from server.helpers import HTMLHelper
from server.decorators import return_on_error

class MangaParser:
    def __init__(self, query: str):
        self.query = query
        self.html_helper = HTMLHelper()
        self.base_url = f"https://mangareader.to/{self.query}"
        self.parser = self.html_helper.get_parser(self.base_url)

    @property
    @return_on_error(None)
    def get_title(self):
        node = self.parser.css_first(".anisc-detail .manga-name")
        return node.text(strip=True) if node else None

    @property
    @return_on_error(None)
    def get_slug(self):
        return self.query

    @property
    @return_on_error(None)
    def get_alt_title(self):
        node = self.parser.css_first(".anisc-detail .manga-name-or")
        return node.text(strip=True)

    @property
    @return_on_error(None)
    def get_type(self):
        node = self.parser.select("span").text_contains("Type:").matches[0].parent.css_first(".name")
        return node.text(strip=True).lower()

    @property
    @return_on_error(None)
    def get_status(self):
        node = self.parser.select("span").text_contains("Status:").matches[0].parent.css_first(".name")
        return node.text(strip=True).lower()

    @property
    @return_on_error(None)
    def get_authors(self):
        node = self.parser.select("span").text_contains("Authors:").matches[0].parent.css_first("a")
        return node.text(strip=True)

    @property
    @return_on_error(None)
    def get_published_date(self):
        node = self.parser.select("span").text_contains("Published:").matches[0].parent.css_first(".name")
        # if node is "?"
        if node.text(strip=True) == "?":
            return None
        return node.text(strip=True).split("to")[0].strip()

    @property
    @return_on_error([])
    def get_genres(self):
        node_list = self.parser.css(".anisc-detail .genres a")
        return [node.text(strip=True).lower() for node in node_list]

    @property
    @return_on_error(None)
    def get_score(self):
        node = self.parser.select("span").text_contains("Score:").matches[0].parent.css_first(".name")
        return node.text(strip=True)

    @property
    @return_on_error(None)
    def get_cover(self):
        node = self.parser.css_first(".anisc-poster .manga-poster-img")
        return node.attributes.get("src")

    @property
    @return_on_error(None)
    def get_synopsis(self):
        node = self.parser.css_first(".modal-content .description-modal")
        return node.text(strip=True)

    def build_dict(self):
        manga_dict = {
            "title": self.get_title,
            "slug": self.get_slug,
            "alt_title": self.get_alt_title,
            "type": self.get_type,
            "status": self.get_status,
            "authors": self.get_authors,
            "published_date": self.get_published_date,
            "genres": self.get_genres,
            "score": self.get_score,
            "cover": self.get_cover,
            "synopsis": self.get_synopsis
        }
        return manga_dict
