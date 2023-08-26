import requests
from bs4 import BeautifulSoup

def isfloat(str: str) -> bool:
    try:
        float(str)
        return True
    except ValueError: return False

# Scrape popular mangas
class PopularManagasScraper:
    def __init__(self):
        self.URL = "https://mangareader.to/home"

    def _scrape_text(self, element, selector):
        selected_element = element.select_one(selector)
        return selected_element.text.strip() if selected_element else None

    def _scrape_numeric(self, element, selector):
        selected_value = self._scrape_text(element, selector)
        print(selected_value)
        if selected_value:
            for value in selected_value.split():
                if isfloat(value) or value.isdigit(): return float(value)
        return None

    def _scrape_ranking(self, element):
        ranking = self._scrape_text(element, ".number span")
        return int(ranking) if ranking else None

    def _scrape_title(self, element):
        return self._scrape_text(element, ".anime-name")

    def _scrape_link(self, element):
        link = element.find("a", class_="link-mask")["href"]
        slug = link.replace("/", "")
        return slug if slug else None

    def _scrape_image(self, element):
        cover = element.find("img", "manga-poster-img")
        return cover["src"] if cover else None

    def _scrape_rating(self, element):
        rating = self._scrape_text(element, ".mp-desc p:nth-of-type(2)")
        return float(rating) if rating else None

    def _scrape_chapters(self, element):
        return self._scrape_numeric(element, ".mp-desc p:nth-of-type(4)")

    def _scrape_volumes(self, element):
        return self._scrape_numeric(element, ".mp-desc p:nth-of-type(5)")

    def scrape(self):
        data = []

        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        container = soup.find("div", {"id": "manga-trending"})

        if container:
            element_list = container.find_all("div", class_="swiper-slide")

            for element in element_list:
                manga_data = {
                    "rank": self._scrape_ranking(element),
                    "title": self._scrape_title(element),
                    "slug": self._scrape_link(element),
                    "cover": self._scrape_image(element),
                    "rating": self._scrape_rating(element),
                    "chapters": self._scrape_chapters(element),
                    "volumes": self._scrape_volumes(element)
                }

                data.append(manga_data)
        return data