import requests
from selectolax.parser import HTMLParser


class HTMLHelper:
    @staticmethod
    def get_parser(url: str) -> HTMLParser:
        res = requests.get(url)
        return HTMLParser(res.content)
