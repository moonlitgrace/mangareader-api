from .base import BaseMangaScraper

class RandomScraper(BaseMangaScraper):
    def __init__(self) -> None:
        super().__init__(url="https://mangareader.to/random/")

    def scrape(self) -> dict:
        node = self.parser.css_first("#ani_detail")
        return self.build_dict(node)