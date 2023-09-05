from .base_manga import BaseMangaScraper

class MangaScraper(BaseMangaScraper):
	def __init__(self, slug: str) -> None:
		self.slug = slug
		super().__init__(url=f"https://mangareader.to/{self.slug}")

	def scrape(self) -> dict:
		return self.build_dict()