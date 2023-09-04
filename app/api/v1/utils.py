import re
from selectolax.parser import Node

# Scraper funcions
def get_text(node: Node, selector: str):
	""" get text from a node according to css selector """
	element = node.css_first(selector)
	return element.text() if element else None

def get_attribute(node: Node, selector: str, attribute: str):
	""" get content from a node according to css selector and attribute """
	element = node.css_first(selector)
	return element.attributes[attribute] if element else None

# Other functions
def slugify(str: str, symbol: str):
	""" Makes lowercase and strip spaces and replace space between words with "+" symbol """
	str = str.lower().strip()
	str = re.sub(r'[^\w\s-]', '', str)
	str = re.sub(r'[\s_-]+', f'{symbol}', str)
	str = re.sub(r'^-+|-+$', '', str)
	return str