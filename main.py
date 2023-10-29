from utils.data_collection import fetch_with_retries
from utils.data_preprocessing import preprocess_text
from models.basic_model import predict_sentiment

def main():
    # Specify the URL of the article you want to analyze
    url = "https://edition.cnn.com/2023/10/29/sport/jude-bellingham-el-clasico-real-madrid-spt-intl/index.html"
    raw_article_text = fetch_with_retries(url)
    preprocessed_article = preprocess_text(raw_article_text)
    sentiment = predict_sentiment(preprocessed_article)
    print(f"Predicted Sentiment (1-5): {sentiment}")

if __name__ == "__main__":
    main()