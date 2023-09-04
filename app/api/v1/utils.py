import re

def slugify(str: str, symbol: str):
	""" Makes lowercase and strip spaces and replace space between words with "+" symbol """
	str = str.lower().strip()
	str = re.sub(r'[^\w\s-]', '', str)
	str = re.sub(r'[\s_-]+', f'{symbol}', str)
	str = re.sub(r'^-+|-+$', '', str)

	return str