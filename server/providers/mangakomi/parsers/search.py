from server.helpers import HTMLHelper
from server.decorators import return_on_error
from selectolax.parser import Node


class SearchParser:
    def __init__(self, query: str, api_url: str) -> None:
        # TODO: pagination logic
        self.api_url = api_url
        self.provider_url = "https://mangakomi.io"
        self.base_url = f"{self.provider_url}/page/1/?s={query}&post_type=wp-manga"
        # facades
        self.html_helper = HTMLHelper()
        self.parser = self.html_helper.get_parser(self.base_url)

    @return_on_error("")
    def get_title(self, container: Node):
        node = container.css_first(".post-title h3")
        return node.text(strip=True)

    @return_on_error("")
    def get_slug(self, container: Node):
        node = container.css_first(".post-title h3 a")
        return node.attributes.get("href").split("/")[-2]

    @return_on_error([])
    def get_genres(self, container: Node):
        node_list = container.css(".mg_genres a")
        return [node.text(strip=True) for node in node_list]

    @return_on_error("")
    def get_chapters(self, container: Node):
        node = container.css_first(".chapter a")
        return node.text(strip=True).split(" ")[1]

    @return_on_error("")
    def get_cover(self, container: Node):
        node = container.css_first(".tab-thumb img")
        return node.attributes.get("data-src")

    @return_on_error("")
    def get_provider_url(self, container: Node):
        slug = self.get_slug(container)
        url = f"{self.provider_url}/{slug}"
        return url

    @return_on_error("")
    def get_manga_url(self, container: Node):
        slug = self.get_slug(container)
        url = f"{self.api_url}mangakomi/manga/{slug}"
        return url

    def build_list(self):
        mangas_list = []
        container_list = self.parser.css(".c-tabs-item .c-tabs-item__content")
        for container in container_list:
            mangas_list.append(
                {
                    "title": self.get_title(container),
                    "slug": self.get_slug(container),
                    "genres": self.get_genres(container),
                    "chapters": self.get_chapters(container),
                    "cover": self.get_cover(container),
                    "provider_url": self.get_provider_url(container),
                    "manga_url": self.get_manga_url(container),
                }
            )
        return mangas_list
