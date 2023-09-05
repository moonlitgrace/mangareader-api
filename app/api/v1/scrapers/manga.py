from .base_manga import BaseMangaScraper

class MangaScraper(BaseMangaScraper):
	def __init__(self, slug: str) -> None:
		# get parser
		self.slug = slug
		# pass url to BaseMangaScraper
		super().__init__(url=f"https://mangareader.to/{self.slug}")

	def scrape(self) -> dict:
		node = self.parser.css_first("#ani_detail")
		manga_dict = {
			"manga_id": self.slug.split("-")[-1],
			**self.build_dict(node)
		}

		return manga_dict