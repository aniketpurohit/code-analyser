# web_scraper.py

import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string
    except requests.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    url = "https://www.example.com"  # Replace with the URL you want to scrape
    print(f"Title of the page: {scrape_website(url)}")
