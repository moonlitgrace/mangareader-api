from server.helpers import HTMLHelper
from server.decorators import return_on_error


class MangaParser:
    def __init__(self, query: str) -> None:
        self.query = query
        self.base_url = f"https://mangakomi.io/manga/{query}/"
        self.html_helper = HTMLHelper()
        self.parser = self.html_helper.get_parser(self.base_url)

    @property
    @return_on_error("")
    def get_title(self):
        node = self.parser.css_first(".post-title h1")
        return node.text(strip=True)

    @property
    @return_on_error("")
    def get_alt_title(self):
        node = self.parser.select(".summary-content").text_contains("Japanese").matches[0]
        return node.text(strip=True).split("(")[0].strip()

    @property
    @return_on_error("")
    def get_status(self):
        node = self.parser.css_first(".post-status .summary-content")
        return node.text(strip=True).lower()

    @property
    @return_on_error("")
    def get_author(self):
        node = self.parser.css_first(".author-content a")
        return node.text(strip=True)

    @property
    @return_on_error([])
    def get_genres(self):
        node_list = self.parser.css(".genres-content a")
        return [node.text(strip=True).lower() for node in node_list]

    @property
    @return_on_error("")
    def get_score(self):
        node = self.parser.css_first(".score")
        return node.text(strip=True)

    @property
    @return_on_error("")
    def get_cover(self):
        node = self.parser.css_first(".summary_image img")
        return node.attributes.get("data-src")

    @property
    @return_on_error("")
    def get_synopsis(self):
        node = self.parser.css_first(".summary__content p")
        return node.text(strip=True)

    def build_dict(self):
        manga_dict = {
            "title": self.get_title,
            "slug": self.query,
            "alt_title": self.get_alt_title,
            "status": self.get_status,
            "author": self.get_author,
            "genres": self.get_genres,
            "score": self.get_score,
            "cover": self.get_cover,
            "synopsis": self.get_synopsis,
            "provider_url": self.base_url,
        }
        return manga_dict
