from typing import Text
from fastapi import responses
import requests
from bs4 import BeautifulSoup
from app.utils import isfloat

# Scrape popular mangas
class PopularScraper:
    def __init__(self):
        super().__init__()
        # Base url to scrape
        self.URL = "https://mangareader.to/home"
        # Selectors
        self.TITLE_SELECTOR = ".anime-name"
        self.LINK_SELECTOR = "a.link-mask"
        self.IMAGE_SELECTOR = "img.manga-poster-img"
        self.RATING_SELECTOR = ".mp-desc p:nth-of-type(2)"
        self.CHAPTERS_SELECTOR = ".mp-desc p:nth-of-type(4)"
        self.VOLUMES_SELECTOR = ".mp-desc p:nth-of-type(5)"

    def _scrape_text(self, element, selector):
        selected_element = element.select_one(selector)
        return selected_element.text.strip() if selected_element else None

    def _scrape_numeric(self, element, selector):
        selected_value = self._scrape_text(element, selector)
        if selected_value:
            for value in selected_value.split():
                if isfloat(value) or value.isdigit(): return float(value)
        return None

    def _scrape_title(self, element):
        return self._scrape_text(element, self.TITLE_SELECTOR)

    def _scrape_link(self, element):
        link = element.select_one(self.LINK_SELECTOR)["href"]
        slug = link.replace("/", "")
        return slug if slug else None

    def _scrape_image(self, element):
        cover = element.select_one(self.IMAGE_SELECTOR)
        return cover["src"] if cover else None

    def _scrape_rating(self, element):
        rating = self._scrape_text(element, self.RATING_SELECTOR)
        return float(rating) if rating else None

    def _scrape_chapters(self, element):
        return self._scrape_numeric(element, self.CHAPTERS_SELECTOR)

    def _scrape_volumes(self, element):
        return self._scrape_numeric(element, self.VOLUMES_SELECTOR)

    def scrape(self):
        data = []

        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        container = soup.select_one("#manga-trending")

        if container:
            element_list = container.find_all("div", class_="swiper-slide")

            for rank, element in enumerate(element_list, start=1):
                manga_data = {
                    "rank": rank,
                    "title": self._scrape_title(element),
                    "slug": self._scrape_link(element),
                    "cover": self._scrape_image(element),
                    "rating": self._scrape_rating(element),
                    "chapters": self._scrape_chapters(element),
                    "volumes": self._scrape_volumes(element)
                }

                data.append(manga_data)
        return data

# Scrape topten mangas
class TopTenScraper():
    def __init__(self):
        super().__init__()
        # Base url to scrape
        self.URL = "https://mangareader.to/home"
        # Selectors
        self.TITLE_SELECTOR = ".desi-head-title a"
        self.IMAGE_SELECTOR = "img.manga-poster-img"
        self.CHAPTER_SELECTOR = ".desi-sub-text"
        self.SYNOPSIS_SELECTOR = ".sc-detail .scd-item"
        self.GENRES_SELECTOR = ".sc-detail .scd-genres span"

    def _scrape_text(self, element, selector):
        selected_element = element.select_one(selector)
        return selected_element.text.strip() if selected_element else None

    def _scrape_numeric(self, element, selector):
        selected_value = self._scrape_text(element, selector)
        if selected_value:
            for value in selected_value.split():
                if isfloat(value) or value.isdigit(): return float(value)
        return None

    def _scrape_title(self, element):
        title = element.select_one(self.TITLE_SELECTOR).text
        return title if title else None

    def _scrape_slug(self, element):
        link = element.select_one(self.TITLE_SELECTOR)["href"]
        slug = link.replace("/", "")
        return slug if slug else None

    def _scrape_cover(self, element):
        cover = element.select_one(self.IMAGE_SELECTOR)
        return cover["src"] if cover else None

    def _scrape_chapter(self, element):
        return self._scrape_numeric(element, self.CHAPTER_SELECTOR)

    def _scrape_synopsis(self, element):
        return self._scrape_text(element, self.SYNOPSIS_SELECTOR)

    def _scrape_genres(self, element):
        genres_list = element.select(self.GENRES_SELECTOR)
        return [genre.text for genre in genres_list]

    def scrape(self):
        data = []

        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        container = soup.select_one(".deslide-wrap #slider .swiper-wrapper")

        if container:
            element_list = container.find_all("div", class_="swiper-slide")

            for rank, element in enumerate(element_list, start=1):
                manga_data = {
                    "rank": rank,
                    "title": self._scrape_title(element),
                    "slug": self._scrape_slug(element),
                    "cover": self._scrape_cover(element),
                    "chapter": self._scrape_chapter(element),
                    "synopsis": self._scrape_synopsis(element),
                    "genres": self._scrape_genres(element)
                }

                data.append(manga_data)
        return data

# Scrape most viewed mangas
class MostViewedScraper():
    def __init__(self) -> None:
        super().__init__()
        # Base url
        self.URL = "https://mangareader.to/home"

    def _scrape_text(self, element, selector):
        selected_element = element.select_one(selector)
        return selected_element.text.strip() if selected_element else None

    def _scrape_numeric(self, element, selector):
        selected_value = self._scrape_text(element, selector)
        if selected_value:
            for value in selected_value.split():
                if isfloat(value) or value.isdigit(): return float(value)
        return None

    def _scrape_title(self, element):
        return self._scrape_text(element, ".manga-detail .manga-name a")

    def _scrape_slug(self, element):
        link = element.select_one(".manga-detail .manga-name a")["href"]
        slug = link.replace("/", "")
        return slug if slug else None

    def _scrape_cover(self, element):
        cover = element.select_one("img.manga-poster-img")["src"]
        cover_high_res = cover.replace("200x300", "500x800")
        return cover_high_res if cover_high_res else None

    def _scrape_views(self, element):
        return self._scrape_numeric(element, ".fd-infor span.fdi-view")

    def scrape_today(self):
        data = []

        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        container = soup.select_one("#main-sidebar #chart-today")

        if container:
            element_list = container.select("ul > li")
            for rank, element in enumerate(element_list, start=1):
                manga_data = {
                    "rank": rank,
                    "title": self._scrape_title(element),
                    "slug": self._scrape_slug(element),
                    "cover": self._scrape_cover(element),
                    "views": self._scrape_views(element)
                }

                data.append(manga_data)
        return data

    def scrape_week(self):
        pass

    def scrape_month(self):
        pass