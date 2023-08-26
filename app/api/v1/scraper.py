import requests
from bs4 import BeautifulSoup

# Scrape popular mangas
class PopularManagasScraper:
    def __init__(self):
        self.URL = "https://mangareader.to/home"

    def scrape(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        manga_trending_container = soup.find("div", {"id": "manga-trending"})

        swiper_slides = manga_trending_container.find_all("div", {"class": "swiper-slide"})

        return len(swiper_slides)