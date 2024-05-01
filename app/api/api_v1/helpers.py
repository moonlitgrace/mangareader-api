from selectolax.parser import HTMLParser
import httpx


class HTMLParserHelper:
    @staticmethod
    def get_parser(url: str):
        html = httpx.get(url)
        return HTMLParser(html.text)
