from tools import ScraperTool, ParserTool, DatabaseTool

# Instantiate tools
scraper = ScraperTool()
parser = ParserTool()
storage = DatabaseTool()

# Test URL:
test_url = "https://en.wikipedia.org/wiki/Tanzania"

# Run the pipeline
print("Starting Web Scraping Simulation...\n")
html_content = scraper.scrape(test_url)
if html_content:
    print("\nSuccessfully scraped the website. First 500 characters of HTML:")
    print(html_content[:500])  # Print first 500 characters of HTML
else:
    print("\nFailed to scrape any data.")

if html_content:
    structured_data = parser.parse(html_content)
    storage.store(structured_data)

    print("\n Web Scraping Simulation Completed!")
    print(f"Extracted {len(structured_data)} courses.")
else:
    print("\n Failed to scrape data.")
