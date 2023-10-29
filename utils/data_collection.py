import requests
from bs4 import BeautifulSoup

def fetch_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Depending on the website's structure, you might need to modify the selector
    paragraphs = soup.select('p')
    article_text = ' '.join(p.text for p in paragraphs)
    
    return article_text

# Test
url = 'https://edition.cnn.com/2023/10/29/opinions/deepfake-pornography-thriving-business-compton-hamlyn/index.html'
print(fetch_article(url))