from server.helpers import HTMLHelper


class MangaParser:
    def __init__(self, query: str) -> None:
        self.query = query
        self.base_url = f"https://mangakomi.io/manga/{query}/"
        self.html_helper = HTMLHelper()
        self.parser = self.html_helper.get_parser(self.base_url)

    def build_dict(self):
        manga_dict = {
            "title": "Testing",
        }
        return manga_dict
