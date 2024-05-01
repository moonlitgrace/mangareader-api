import re
import html
from urllib.parse import urlparse


# String Helper
class StringHelper:
    @staticmethod
    def clean(string: str) -> str:
        # Convert any HTML line breaks to newlines
        string = re.sub(r"<br\s*/?>", "\n", string)
        # Convert non-breaking spaces to spaces
        string = string.replace("\xa0", " ")
        # Strip any remaining HTML tags
        string = html.unescape(string)
        string = re.sub(r"<[^>]*>", "", string)
        # Remove newlines at the end
        string = string.rstrip("\n")
        # Remove newlines at the start
        string = string.lstrip("\n")
        # Trim whitespace
        string = string.strip()
        # Remove backslashes
        string = string.replace("\\", "")
        return string

    @staticmethod
    def is_url(string: str) -> bool:
        # Try to parse string as url
        try:
            url = urlparse(string)
            return all([url.scheme, url.netloc])
        except ValueError:
            return False

    @staticmethod
    def slugify(string: str, symbol: str) -> str:
        """Makes lowercase and strip spaces and replace space between words with "+" symbol"""
        string = string.lower().strip()
        string = re.sub(r"[^\w\s-]", "", string)
        string = re.sub(r"[\s_-]+", f"{symbol}", string)
        string = re.sub(r"^-+|-+$", "", string)
        return string

# Response Helper
class ResponseHelper:
    @staticmethod
    def format_response(data, next=None, prev=None):
        response = {
            "count": len(data),
            "next": next,
            "prev": prev,
            "data": data,
        }

        return response
