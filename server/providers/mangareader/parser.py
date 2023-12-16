from ...helpers import HTMLHelper


class MangaReader:
    def __init__(self):
        self.html_helper = HTMLHelper()
        self.base_url = "https://mangareader.to"

    def get_manga(self, query: str):
        parse_url = f"{self.base_url}/{query}"
        _ = self.html_helper.get_parser(parse_url)

        manga_dict = {}
        manga_dict["title"] = _.css_first(
            ".anisc-detail .manga-name").text(strip=True)

        return manga_dict
