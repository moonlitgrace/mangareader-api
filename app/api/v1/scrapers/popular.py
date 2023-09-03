from fastapi.responses import JSONResponse
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
	def __get_text(node: Node, selector: str):
		element = node.css_first(selector)
		return element.text() if element else None

	@staticmethod
	def __get_attribute(node: Node, selector: str, attribute: str):
		element = node.css_first(selector)
		return element.attributes[attribute] if element else None

	def __get_slug(self, node: Node):
		slug = self.__get_attribute(node, "a.link-mask", "href")
		return slug.replace("/", "") if slug else None

	def __get_langs(self, node: Node):
		langs = self.__get_text(node, ".mp-desc p:nth-of-type(3)")
		return langs.split("/") if langs else None

	def __get_chapters_volumes(self, node: Node, index: int):
		data = self.__get_text(node, f".mp-desc p:nth-of-type({index})")
		if data:
			total = data.split()[1]
			lang = data.split()[2].translate(str.maketrans("", "", "[]"))

			data_dict = {
				"total": total,
				"lang": lang
			}

			return data_dict
		return None

	def __build_dict(self, node):
		manga_dict = {
			"rank": self.__get_text(node, ".number span"),
			"title": self.__get_text(node, ".anime-name"),
			"slug": self.__get_slug(node),
			"cover": self.__get_attribute(node, "img.manga-poster-img", "src"),
			"rating": self.__get_text(node, ".mp-desc p:nth-of-type(2)"),
			"langs": self.__get_langs(node),
			"chapters": self.__get_chapters_volumes(node, 4),
			"volumes": self.__get_chapters_volumes(node, 5)
		}

		return manga_dict

	def parse(self):
		try:
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
		except Exception as e:
			error = "Couldn't connect to website"
			message = "Something went wrong while trying to scrape, please try again later!"
			status_code = 503

			return JSONResponse(
                content = {
                    "detail": {
                        "error": error,
                        "message": message,
                        "status_code": status_code
                    }
                },
                status_code=status_code
            )