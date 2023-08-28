from selectolax.parser import HTMLParser, Node
import requests

class MostViewedScraper:
	# Charts
	# eg. "today" | "week" | "month"
	CHARTS = ["today", "week", "month"]

	def __init__(self):
		super().__init__()

		# get parser
		self.parser = self.__get_parser()

	@staticmethod
	def __get_parser():
		url = "https://mangareader.to/home"
		res = requests.get(url)

		return HTMLParser(res.content)

	@staticmethod
	def __get_text(node: Node, selector: str):
		element = node.css_first(selector)
		return element.text() if element else None

	@staticmethod
	def __get_attribute(node: Node, selector: str, attribute: str):
		element = node.css_first(selector)
		return element.attributes[attribute] if element else None

	def __get_slug(self, node: Node):
		slug = self.__get_attribute(node, ".manga-detail .manga-name a", "href")
		return slug.replace("/", "") if slug else None

	def __get_cover(self, node: Node):
		cover = self.__get_attribute(node, "img.manga-poster-img", "src")
		return cover.replace("200x300", "500x800") if cover else None

	def __build_dict(self, node: Node):
		manga_dict = {
			"rank":	self.__get_text(node, ".ranking-number span"),
			"title": self.__get_text(node, ".manga-detail .manga-name a"),
			"slug": self.__get_slug(node),
			"cover": self.__get_cover(node)
		}

		return manga_dict

	def parse(self, chart):
		mangas_list = []

		container = self.parser.css_first(f"#main-sidebar #chart-{chart}")
		node_list = container.css("ul > li")

		for index, node in enumerate(node_list, start=1):
			manga_dict = {
				"id": index,
				**self.__build_dict(node)
			}

			mangas_list.append(manga_dict)
		return mangas_list