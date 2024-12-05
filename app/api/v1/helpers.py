import httpx
from selectolax.parser import HTMLParser


class HTMLParserHelper:
    @staticmethod
    def get_parser(url: str):
        html = httpx.get(url)
        return HTMLParser(html.text)
