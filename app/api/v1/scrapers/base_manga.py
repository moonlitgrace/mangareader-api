import requests
from selectolax.parser import HTMLParser, Node
from ..utils import get_attribute, get_text
from ..decorators import return_on_error

class BaseMangaScraper:
    def __init__(self, url: str) -> None:
        self.url = url
        # get parser
        self.parser = self.__get_parser()

    def __get_parser(self) -> HTMLParser:
        res = requests.get(self.url)
        return HTMLParser(res.content)

    @property
    def get_manga_id(self) -> str:
        node = self.parser.css_first("meta[property='og:url']")
        slug = node.attributes["content"]
        return slug.split("-")[-1] if slug else ""

    @property
    @return_on_error("")
    def get_title(self) -> str:
        node = self.parser.css_first(".anisc-detail .manga-name")
        return node.text(strip=True)

    @property
    @return_on_error("")
    def get_alt_title(self):
        node = self.parser.css_first(".anisc-detail .manga-name-or")
        return node.text(strip=True)

    @property
    def get_slug(self) -> str:
        node = self.parser.css_first("#ani_detail .ani_detail-stage .anis-content .anisc-detail .manga-buttons a")
        slug = node.attributes["href"]
        return slug.split("/")[-1] if slug else ""

    @property
    @return_on_error("")
    def get_manga_type(self):
        node = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(1) a")
        return node.text(strip=True).lower()

    @property
    @return_on_error("")
    def get_status(self):
        node = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(2) .name")
        return node.text(strip=True).lower()

    @property
    @return_on_error([])
    def get_genres(self) -> list:
        genres = self.parser.css(".anisc-detail .sort-desc .genres a")
        return [genre.text(strip=True) for genre in genres]

    @property
    @return_on_error([])
    def get_authers(self) -> list:
        authers = self.parser.css(".anisc-detail .anisc-info .item:nth-child(3) a")
        return [auther.text(strip=True) for auther in authers]

    @property
    @return_on_error([])
    def get_magazines(self) -> list:
        magazines = self.parser.css(".anisc-detail .anisc-info .item:nth-child(4) a")
        return [magazine.text() for magazine in magazines]

    @property
    @return_on_error("")
    def get_published(self) -> str:
        published_string = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(5) .name")
        return published_string.text(strip=True).split(" to ")[0]

    @property
    @return_on_error("")
    def get_score(self):
        node = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(6) .name")
        return node.text(strip=True)

    @property
    @return_on_error("")
    def get_views(self) -> str:
        views_string = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(7) .name")
        return views_string.text(strip=True).replace(",", "")

    @property
    @return_on_error("")
    def get_manga_cover(self):
        node = self.parser.css_first(".anisc-poster .manga-poster-img")
        image = node.attributes["src"]
        return image

    @property
    @return_on_error("")
    def get_synopsis(self):
        node = self.parser.css_first(".anisc-detail .sort-desc .description")
        return node.text(strip=True)

    @property
    @return_on_error([])
    def get_chapters(self) -> list:
        items = self.parser.css(f"#main-content #list-chapter .dropdown-menu a")

        item_list = []
        for item in items:
            text = item.text().translate(str.maketrans("", "", "[]()"))

            item_dict = {
                "total": text.split()[2],
                "lang": text.split()[0]
            }

            item_list.append(item_dict)
        return item_list

    @property
    @return_on_error([])
    def get_volumes(self) -> list:
        items = self.parser.css(f"#main-content #list-vol .dropdown-menu a")

        item_list = []
        for item in items:
            text = item.text().translate(str.maketrans("", "", "[]()"))

            item_dict = {
                "total": text.split()[2],
                "lang": text.split()[0]
            }

            item_list.append(item_dict)
        return item_list

    def build_dict(self) -> dict:
        manga_dict = {
            "manga_id": self.get_manga_id,
            "title": self.get_title,
            "alt_title": self.get_alt_title,
            "slug": self.get_slug,
            "type": self.get_manga_type,
            "status": self.get_status,
            "published": self.get_published,
            "score": self.get_score,
            "views": self.get_views,
            "cover": self.get_manga_cover,
            "synopsis": self.get_synopsis,
            "genres": self.get_genres,
            "authers": self.get_authers,
            "mangazines": self.get_magazines,
            "chapters": self.get_chapters,
            "volumes": self.get_volumes
        }

        return manga_dict