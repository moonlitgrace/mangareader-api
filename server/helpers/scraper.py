from typing import Optional
from selectolax.parser import Node


class ScrapeHelper:
    @staticmethod
    def get_text(node: Node, selector: str) -> Optional[str]:
        element = node.css_first(selector)
        return element.text().strip() if element else None

    @staticmethod
    def get_attribute(node: Node, selector: str, attribute: str) -> Optional[str]:
        element = node.css_first(selector)
        return element.attributes[attribute] if element else None
