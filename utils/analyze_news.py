import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_collection import fetch_with_retries
from data_preprocessing import preprocess_text
from models.basic_model import predict_sentiment
from dotenv import load_dotenv

# Explicitly provide path to .env; adjust the path if needed
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Debug
# print(sys.executable)

def analyze_news(url):
    # Specify the URL of the article you want to analyze
    raw_article_text = fetch_with_retries(url)
    preprocessed_article = preprocess_text(raw_article_text)
    sentiment = predict_sentiment(preprocessed_article)
    print(f"Predicted Sentiment: {sentiment}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Debug
        # print(f"Received URL: {sys.argv[1]}")
        analyze_news(sys.argv[1])
    else:
        print("No URL argument provided.")
