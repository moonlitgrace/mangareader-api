from ..models.base_manga import MangaModel
from ..decorators.return_decorator import return_on_error
from ..helpers.string import StringHelper
from ..helpers.html_helper import HTMLHelper


class BaseMangaScraper:
    def __init__(self, url: str) -> None:
        # Facades
        self.string_helper = StringHelper()
        self.html_helper = HTMLHelper()
        # Parser
        self.parser = self.html_helper.get_parser(url)

    @property
    @return_on_error(0)
    def __get_manga_id(self):
        node = self.parser.css_first("meta[property='og:url']")
        slug = node.attributes["content"]
        if slug:
            try:
                manga_id = slug.split("-")[-1]
                return int(manga_id)
            except ValueError:
                return 0

    @property
    @return_on_error("")
    def __get_title(self):
        node = self.parser.css_first(".anisc-detail .manga-name")
        return node.text(strip=True)

    @property
    @return_on_error("")
    def __get_alt_title(self):
        node = self.parser.css_first(".anisc-detail .manga-name-or")
        return node.text(strip=True)

    @property
    @return_on_error("")
    def __get_slug(self):
        node = self.parser.css_first(
            "#ani_detail .ani_detail-stage .anis-content .anisc-detail .manga-buttons a"
        )
        slug = node.attributes["href"]
        return slug.split("/")[-1] if slug else ""

    @property
    @return_on_error("")
    def __get_manga_type(self):
        node = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(1) a")
        return node.text(strip=True).lower()

    @property
    @return_on_error("")
    def __get_status(self):
        node = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(2) .name")
        return node.text(strip=True).lower()

    @property
    @return_on_error([])
    def __get_genres(self):
        genres = self.parser.css(".anisc-detail .sort-desc .genres a")
        return [genre.text(strip=True) for genre in genres]

    @property
    @return_on_error([])
    def __get_authers(self):
        authers = self.parser.css(".anisc-detail .anisc-info .item:nth-child(3) a")
        return [auther.text(strip=True) for auther in authers]

    @property
    @return_on_error([])
    def __get_magazines(self):
        magazines = self.parser.css(".anisc-detail .anisc-info .item:nth-child(4) a")
        return [magazine.text() for magazine in magazines]

    @property
    @return_on_error("")
    def __get_published(self):
        published_string = self.parser.css_first(
            ".anisc-detail .anisc-info .item:nth-child(5) .name"
        )
        return published_string.text(strip=True).split(" to ")[0]

    @property
    @return_on_error(0)
    def __get_score(self):
        node = self.parser.css_first(".anisc-detail .anisc-info .item:nth-child(6) .name")
        return node.text(strip=True)

    @property
    @return_on_error(0)
    def __get_views(self):
        views_string = self.parser.css_first(
            ".anisc-detail .anisc-info .item:nth-child(7) .name"
        )
        return views_string.text(strip=True).replace(",", "")

    @property
    @return_on_error("")
    def __get_manga_cover(self):
        node = self.parser.css_first(".anisc-poster .manga-poster-img")
        image = node.attributes["src"]
        return image

    @property
    @return_on_error("")
    def __get_synopsis(self):
        node = self.parser.css_first(".anisc-detail .sort-desc .description")
        return self.string_helper.clean(node.text())

    @property
    @return_on_error([])
    def __get_chapters(self):
        items = self.parser.css(f"#main-content #list-chapter .dropdown-menu a")

        item_list = []
        for item in items:
            text = item.text().translate(str.maketrans("", "", "[]()"))

            item_dict = {"total": text.split()[2], "lang": text.split()[0]}

            item_list.append(item_dict)
        return item_list

    @property
    @return_on_error([])
    def __get_volumes(self):
        items = self.parser.css(f"#main-content #list-vol .dropdown-menu a")

        item_list = []
        for item in items:
            text = item.text().translate(str.maketrans("", "", "[]()"))

            item_dict = {"total": text.split()[2], "lang": text.split()[0]}

            item_list.append(item_dict)
        return item_list

    @property
    @return_on_error({})
    def scrape(self) -> dict:
        manga_dict = {
            "manga_id": self.__get_manga_id,
            "title": self.__get_title,
            "alt_title": self.__get_alt_title,
            "slug": self.__get_slug,
            "type": self.__get_manga_type,
            "status": self.__get_status,
            "published": self.__get_published,
            "score": self.__get_score,
            "views": self.__get_views,
            "cover": self.__get_manga_cover,
            "synopsis": self.__get_synopsis,
            "genres": self.__get_genres,
            "authers": self.__get_authers,
            "mangazines": self.__get_magazines,
            "chapters": self.__get_chapters,
            "volumes": self.__get_volumes,
        }

        return manga_dict
