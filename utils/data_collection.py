import requests
from bs4 import BeautifulSoup
import time

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
HEADERS = {"User-Agent": USER_AGENT}
MAX_RETRIES = 3
RETRY_DELAY = 5  # Sekunder

def fetch_article(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.select('p')
    article_text = ' '.join(p.text for p in paragraphs)
    return article_text

def fetch_with_retries(url):
    for attempt in range(MAX_RETRIES):
        try:
            return fetch_article(url)
        except requests.RequestException:
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                raise