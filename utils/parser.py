from typing import Tuple, List
import mysql.connector

class ContentParser:
    def __call__(self, filename: str) -> Tuple[str, List[str], str]:
        with open(filename) as f:
            lines = f.readlines()
            
            date = lines[2].strip()
            assert date[:5] == "Date:"
            if len(date) > len("Date:"):
                date = date[5:].replace(" ", "")
            else:
                date = ""

            tags = lines[3].strip()
            assert tags[:5] == "Tags:"
            if len(tags) > len("Tags:"):
                tags = tags[5:].strip().split(" ")
            else:
                tags = []

            content = lines[4]
            assert content[:8] == "Content:"
            content = "".join(lines[5:])
        return date, tags, content
