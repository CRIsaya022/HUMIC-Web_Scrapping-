import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO)

class ScraperTool:
    def scrape(self, url):
        # Fetch HTML content from the given URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            logging.info(f"Successfully scraped: {url}")
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to scrape {url}: {e}")
            return None



class ParserTool:
    def parse(self, raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        content = {}

        # Extract the title of the page
        title_tag = soup.find("h1", id="firstHeading")
        content["title"] = title_tag.text.strip() if title_tag else "No Title Found"

        # Extract the introductory paragraphs (before first heading)
        intro_paragraphs = []
        for elem in soup.select("div.mw-parser-output > p"):
            text = elem.get_text(strip=True)
            if text:
                intro_paragraphs.append(text)
            # Stop when the first heading is encountered
            if elem.find_next_sibling(["h2", "h3"]):
                break
        content["introduction"] = " ".join(intro_paragraphs)

        # Extract sections and their content
        sections = {}
        current_heading = None
        current_text = []

        for elem in soup.select("div.mw-parser-output > *"):
            if elem.name == "h2":
                # Save previous section
                if current_heading and current_text:
                    sections[current_heading] = " ".join(current_text)
                current_heading = elem.text.strip().replace("[edit]", "")
                current_text = []
            elif elem.name == "p" and current_heading:
                paragraph = elem.get_text(strip=True)
                if paragraph:
                    current_text.append(paragraph)

        # Add last section
        if current_heading and current_text:
            sections[current_heading] = " ".join(current_text)

        content["sections"] = sections
        return content


class DatabaseTool:
    def store(self, data, filename="learning_resources.json"):
        import json
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Data saved to {filename}")

