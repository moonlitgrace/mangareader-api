from ...helpers import HTMLHelper

class MangaReader:
    def __init__(self):
        self.html_helper = HTMLHelper()
        self.base_url = "https://mangareader.to"

    def get_manga(self, query: str):
        parse_url = f"{self.base_url}/{query}"
        _ = self.html_helper.get_parser(parse_url)

        manga_dict = {}
        manga_dict["title"] = _.css_first(".anisc-detail .manga-name").text(strip=True)
        manga_dict["slug"] = query
        manga_dict["alt_title"] = _.css_first(".anisc-detail .manga-name-or").text(strip=True)
        manga_dict["type"] = _.select("span").text_contains("Type:").matches[0].parent.css_first(".name").text(strip=True).lower()
        manga_dict["status"] = _.select("span").text_contains("Status:").matches[0].parent.css_first(".name").text(strip=True).lower()
        manga_dict["authors"] = _.select("span").text_contains("Authors:").matches[0].parent.css_first("a").text(strip=True)
        manga_dict["genres"] = [genre.text(strip=True).lower() for genre in _.css(".anisc-detail .genres a")]
        manga_dict["score"] = _.select("span").text_contains("Score:").matches[0].parent.css_first(".name").text(strip=True)
        manga_dict["cover"] = _.css_first(".anisc-poster .manga-poster-img").attrs.get("src", "")
        manga_dict["synopsis"] = _.css_first(".modal-content .description-modal").text(strip=True)

        return manga_dict
