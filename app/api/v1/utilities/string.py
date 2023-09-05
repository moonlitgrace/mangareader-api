import re
import html

class StringHelper:
    def clean(self, string: str) -> str:
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