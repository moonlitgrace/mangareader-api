from selectolax.parser import HTMLParser, Node
import requests

class MangaScraper():
	def __init__(self, slug: str):
		super().__init__()

		# get parser
		self.slug = slug
		self.parser = self.__get_parser()

	def __get_parser(self):
		url = f"https://mangareader.to/{self.slug}"
		res = requests.get(url)

		return HTMLParser(res.content)

	@staticmethod
	def __get_text(node: Node, selector: str):
		element = node.css_first(selector)
		return element.text().strip() if element else None

	@staticmethod
	def __get_attribute(node: Node, selector: str, attribute: str):
		element = node.css_first(selector)
		return element.attributes[attribute] if element else None

	def __get_genres(self, node: Node):
		genres = node.css(".anisc-detail .sort-desc .genres a")
		return [genre.text() for genre in genres] if genres else None

	def __get_authers(self, node: Node):
		authers = node.css(".anisc-detail .anisc-info .item:nth-child(3) a")
		return [auther.text() for auther in authers] if authers else None

	def __get_magazines(self, node: Node):
		magazines = node.css(".anisc-detail .anisc-info .item:nth-child(4) a")
		return [magazine.text() for magazine in magazines] if magazines else None

	def __get_published(self, node: Node):
		published_string = self.__get_text(node, ".anisc-detail .anisc-info .item:nth-child(5) .name")
		if published_string:
			date = published_string.split(" to ")[0]
			return date
		return None

	def __get_views(self, node: Node):
		views_string = self.__get_text(node, ".anisc-detail .anisc-info .item:nth-child(7) .name")
		return views_string.replace(",", "") if views_string else None

	def __get_chapters_volumes(self, type: str):
		items = self.parser.css(f"#main-content #list-{type} .dropdown-menu a")

		item_list = []
		for item in items:
			text = item.text().translate(str.maketrans("", "", "[]()"))

			item_dict = {
				"total": text.split()[2],
				"lang": text.split()[0]
			}

			item_list.append(item_dict)
		return item_list

	def parse(self):
		node = self.parser.css_first("#ani_detail")

		manga_dict = {
			"id": self.slug.split("-")[-1],
			"title": self.__get_text(node, ".anisc-detail .manga-name"),
			"alt_title": self.__get_text(node, ".anisc-detail .manga-name-or"),
			"slug": self.slug,
			"type": self.__get_text(node, ".anisc-detail .anisc-info .item:nth-child(1) a"),
			"status": self.__get_text(node, ".anisc-detail .anisc-info .item:nth-child(2) .name"),
			"published": self.__get_published(node),
			"score": self.__get_text(node, ".anisc-detail .anisc-info .item:nth-child(6) .name"),
			"views": self.__get_views(node),
			"cover": self.__get_attribute(node, ".anisc-poster .manga-poster-img", "src"),
			"synopsis": self.__get_text(node, ".anisc-detail .sort-desc .description"),
			"genres": self.__get_genres(node),
			"authers": self.__get_authers(node),
			"mangazines": self.__get_magazines(node),
			"chapters": self.__get_chapters_volumes("chapter"),
			"volumes": self.__get_chapters_volumes("vol")
		}

		return manga_dict
