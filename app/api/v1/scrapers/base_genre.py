import requests
from selectolax.parser import HTMLParser, Node
from ..utils import slugify, get_text, get_attribute

class BaseGenreScraper:
	def __init__(self, url: str):
		self.url = url
		self.parser = self.__get_parser()

	def __get_parser(self):
		res = requests.get(self.url)
		return HTMLParser(res.content)

	def __get_id(self, node: Node):
		id = self.__get_slug(node)
		return id.split("-")[-1] if id else None

	def __get_slug(self, node: Node):
		slug = get_attribute(node, ".manga-detail .manga-name a", "href")
		return slug.replace("/", "") if slug else None

	def __get_langs(self, node: Node):
		langs_string = get_text(node, ".manga-poster .tick-lang")
		return langs_string.split("/") if langs_string else None

	def __get_genres(self, node: Node):
		genres = node.css(".manga-detail .fd-infor a")
		return [genre.text() for genre in genres] if genres else None

	def __get_chapters(self, node: Node):
		data = get_text(node, ".manga-detail .fd-list:nth-child(1) .chapter a")
		if data:
			total = data.split()[1]
			lang = data.split()[2].translate(str.maketrans("", "", "[]"))

			data_dict = {
				"total": total,
				"lang": lang
			}

			return data_dict
		return None

	def scrape(self) -> list:
		manga_list = []
		container = self.parser.css_first(".manga_list-sbs")
		node_list = container.css("div.item.item-spc")

		for index, node in enumerate(node_list, start=1):
			manga_dict = {
				"id": index,
				"manga_id": self.__get_id(node),
				"title": get_text(node, ".manga-detail .manga-name a"),
				"slug": self.__get_slug(node),
				"cover": get_attribute(node, ".manga-poster img", "src"),
				"langs": self.__get_langs(node),
				"genres": self.__get_genres(node),
				"chapters": self.__get_chapters(node)
			}

			manga_list.append(manga_dict)
		return manga_list