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

    def build_dict(self):
        manga_dict = {
            "title": self.get_title,
        }
        return manga_dict
