from ...helpers import HTMLHelper
from fastapi.exceptions import HTTPException


class MangaReader:
    def __init__(self):
        self.html_helper = HTMLHelper()
        self.base_url = "https://mangareader.to"

    def get_manga(self, query: str):
        try:
            parse_url = f"{self.base_url}/{query}"
            _ = self.html_helper.get_parser(parse_url)

            manga_dict = {
                "title": _.css_first(".anisc-detail .manga-name").text(strip=True),
                "slug": query,
                "alt_title": _.css_first(".anisc-detail .manga-name-or").text(
                    strip=True
                ),
                "type": (
                    _.select("span")
                    .text_contains("Type:")
                    .matches[0]
                    .parent.css_first(".name")
                    .text(strip=True)
                    .lower()
                ),
                "status": (
                    _.select("span")
                    .text_contains("Status:")
                    .matches[0]
                    .parent.css_first(".name")
                    .text(strip=True)
                    .lower()
                ),
                "authors": (
                    _.select("span")
                    .text_contains("Authors:")
                    .matches[0]
                    .parent.css_first("a")
                    .text(strip=True)
                ),
                "published_date": (
                    _.select("span")
                    .text_contains("Published:")
                    .matches[0]
                    .parent.css_first(".name")
                    .text(strip=True)
                    .split("to")[0]
                    .strip()
                ),
                "genres": [
                    genre.text(strip=True).lower()
                    for genre in _.css(".anisc-detail .genres a")
                ],
                "score": (
                    _.select("span")
                    .text_contains("Score:")
                    .matches[0]
                    .parent.css_first(".name")
                    .text(strip=True)
                ),
                "cover": _.css_first(".anisc-poster .manga-poster-img").attrs.get(
                    "src", ""
                ),
                "synopsis": _.css_first(".modal-content .description-modal").text(
                    strip=True
                ),
            }

            return manga_dict
        except Exception as err:
            print(err)
            raise HTTPException(status_code=404, detail="Page not found! Try another query.")
