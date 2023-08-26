import requests
from bs4 import BeautifulSoup, element

# Scrape popular mangas
class PopularManagasScraper:
    def __init__(self):
        self.URL = "https://mangareader.to/home"

    def _scrape_ranking(self, element):
        ranking_container = element.find("div", class_="number")
        rank = ranking_container.find("span")
        if rank:
            return float(rank.text)
        return "Ranking not found"

    def _scrape_title(self, element):
        title_element = element.find("div", class_="anime-name")
        if title_element:
            return title_element.text.strip()
        return "No title found"

    def _scrape_image(self, element):
        cover = element.find("img", class_="manga-poster-img")
        if cover:
            return cover["src"]
        return "Cover image not found"

    def _scrape_rating(self, element):
        container = element.find("div", class_="mp-desc")
        rating = container.find_all("p")[1].text
        if rating:
            return float(rating)
        return "Rating not found"

    def _scrape_chapters(self, element):
        container = element.find("div", class_="mp-desc")
        chapters_string = container.find_all("p")[3].text
        if chapters_string:
            for string in chapters_string.split():
                if string.isdigit(): return int(string)
        return "Chapters not found"

    def _scrape_volumes(self, element):
        container = element.find("div", class_="mp-desc")
        volumes_string = container.find_all("p")[4].text
        if volumes_string:
            for string in volumes_string.split():
                if string.isdigit(): return int(string)
        return "Volumes not found"

    def _scrape_link(self, element):
        link = element.find("a", class_="link-mask")["href"]
        slug = link.replace("/", "")
        if slug: return slug
        return "Slug not found"

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