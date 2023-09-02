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

	def __get_views(self, node: Node):
		views_string = self.__get_text(node, ".fd-infor .fdi-view")
		if views_string:
			views = views_string.split()[0].replace(",", "")
			return views
		return None

	def __get_langs(self, node: Node):
		langs_string = self.__get_text(node, ".fd-infor > span:nth-child(1)")
		return [lang for lang in langs_string.split("/")] if langs_string else None

	def __get_chapters_volumes(self, node: Node, index: int):
		data_string = self.__get_text(node, f".d-block span:nth-child({index})")
		return data_string.split()[1] if data_string else None

	def __get_genres(self, node: Node):
		genres = node.css(".fd-infor .fdi-cate a")
		return [genre.text() for genre in genres] if genres else None

	def __build_dict(self, node: Node):
		manga_dict = {
			"rank":	self.__get_text(node, ".ranking-number span"),
			"title": self.__get_text(node, ".manga-detail .manga-name a"),
			"slug": self.__get_slug(node),
			"cover": self.__get_cover(node),
			"views": self.__get_views(node),
			"langs": self.__get_langs(node),
			"chapters": self.__get_chapters_volumes(node, 1),
			"volumes": self.__get_chapters_volumes(node, 2),
			"genres": self.__get_genres(node)
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