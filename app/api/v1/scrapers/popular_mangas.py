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
	def __get_ranking(node: Node):
		ranking = node.css_first(".number span")
		return ranking.text() if ranking else None

	@staticmethod
	def __get_title(node: Node):
		title = node.css_first(".anime-name").text()
		return title if title else None

	@staticmethod
	def __get_slug(node: Node):
		slug = node.css_first("a.link-mask").attributes["href"]
		return slug.replace("/", "") if slug else None

	def __get_cover(self, node: Node):
		cover_src = node.css_first("img.manga-poster-img").attributes["src"]
		return cover_src if cover_src else None

	@staticmethod
	def __get_rating(node: Node):
		rating = node.css_first(".mp-desc p:nth-of-type(2)").text()
		return rating if rating else None

	@staticmethod
	def __get_langs(node: Node):
		langs = node.css_first(".mp-desc p:nth-of-type(3)").text().split("/")
		return langs if langs else None

	@staticmethod
	def __get_chapters(node: Node):
		chapters_data = node.css_first(".mp-desc p:nth-of-type(4)").text()
		total_chapters = chapters_data.split()[1]
		# remove "[]" from lang
		translater = str.maketrans("", "", "[]")
		lang = chapters_data.split()[2].translate(translater)

		chapters_dict = {
			"total": total_chapters,
			"lang": lang
		}

		return chapters_dict

	@staticmethod
	def __get_volumes(node: Node):
		chapters_data = node.css_first(".mp-desc p:nth-of-type(5)").text()
		total_chapters = chapters_data.split()[1]
		# remove "[]" from lang
		translater = str.maketrans("", "", "[]")
		lang = chapters_data.split()[2].translate(translater)

		chapters_dict = {
			"total": total_chapters,
			"lang": lang
		}

		return chapters_dict

	def __build_dict(self, node):
		manga_dict = {
			"rank": self.__get_ranking(node),
			"title": self.__get_title(node),
			"slug": self.__get_slug(node),
			"cover": self.__get_cover(node),
			"rating": self.__get_rating(node),
			"langs": self.__get_langs(node),
			"chapters": self.__get_chapters(node),
			"volumes": self.__get_volumes(node)
		}

		return manga_dict

	def parse(self):
		mangas_list = []

		container = self.parser.css_first("div#manga-trending")
		nodes_list = container.css("div.swiper-slide")

		for index, node in enumerate(nodes_list, start=1):
			manga_dict = {
				"id": index,
				**self.__build_dict(node)
			}

			mangas_list.append(manga_dict)

		return mangas_list