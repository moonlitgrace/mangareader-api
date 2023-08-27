import requests
from selectolax.parser import HTMLParser, Node

class PopularScraper:
	def __init__(self) -> None:
		super().__init__()

		# get parser
		self.parser = self.__get_parser()

	@staticmethod
	def __get_parser():
		url = "https://mangareader.to/home"
		res = requests.get(url)

		return HTMLParser(res.content)

	@staticmethod
	def __get_title(element: Node):
		title = element.css_first(".anime-name").text()
		return title if title else None

	@staticmethod
	def __get_slug(element: Node):
		slug = element.css_first("a.link-mask").attributes["href"]
		return slug.replace("/", "") if slug else None

	@staticmethod
	def __get_cover(element: Node):
		cover = element.css_first("img.manga-poster-img").attributes["src"]
		return cover if cover else None

	def __build_dict(self, element):
		manga_dict = {
			"title": self.__get_title(element),
			"slug": self.__get_slug(element),
			"cover": self.__get_cover(element)
		}

		return manga_dict

	def parse(self):
		mangas_list = []

		container = self.parser.css_first("div#manga-trending")
		elements_list = container.css("div.swiper-slide")

		for index, element in enumerate(elements_list, start=1):
			manga_dict = {
				"id": index,
				**self.__build_dict(element)
			}

			mangas_list.append(manga_dict)

		return mangas_list