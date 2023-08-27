from typing import Text
from fastapi import responses
import requests
from bs4 import BeautifulSoup
from app.utils import isfloat

# Scrape most viewed mangas
class MostViewedScraper():
    # Possbile charts
    CHARTS = ["today", "week", "month"]

    def __init__(self) -> None:
        super().__init__()

        self.session = requests.Session()
        # Base url
        self.URL = "https://mangareader.to/home"
        # Css selectors
        self.SELECTORS = {
            "title": ".manga-detail .manga-name a",
            "image": "img.manga-poster-img",
            "views": ".fd-infor .fdi-view",
            "chapters": ".fd-infor .fdi-chapter:nth-child(1)",
            "volumes": ".fd-infor .fdi-chapter:nth-child(2)",
            "genres": ".fd-infor .fdi-cate a"
        }

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
        return self._scrape_text(element, self.SELECTORS["title"])

    def _scrape_slug(self, element):
        link = element.select_one(self.SELECTORS["title"])["href"]
        slug = link.replace("/", "")
        return slug if slug else None

    def _scrape_cover(self, element):
        cover = element.select_one(self.SELECTORS["image"])["src"]
        cover_high_res = cover.replace("200x300", "500x800")
        return cover_high_res if cover_high_res else None

    def _scrape_views(self, element):
        views = self._scrape_text(element, self.SELECTORS["views"])
        if views:
            # Need to do this since res is in this format eg. "10,581 views"
            views = views.split()[0].replace(",", "")
        return views if views else None

    def _scrape_chapters(self, element):
        return self._scrape_numeric(element, self.SELECTORS["chapters"])

    def _scrape_volumes(self, element):
        return self._scrape_numeric(element, self.SELECTORS["volumes"])

    def _scrape_genres(self, element):
        genres = element.select(self.SELECTORS["genres"])
        return [genre.text for genre in genres] if genres else None

    def scrape_chart(self, chart):
        data = []

        response = self.session.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        container = soup.select_one(f"#main-sidebar #chart-{chart}")

        if container:
            element_list = container.select("ul > li")
            for rank, element in enumerate(element_list, start=1):
                manga_data = {
                    "rank": rank,
                    "title": self._scrape_title(element),
                    "slug": self._scrape_slug(element),
                    "cover": self._scrape_cover(element),
                    "views": self._scrape_views(element),
                    "chapters": self._scrape_chapters(element),
                    "volumes": self._scrape_volumes(element),
                    "genres": self._scrape_genres(element)
                }

                data.append(manga_data)
        return data