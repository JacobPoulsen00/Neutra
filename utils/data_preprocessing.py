import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def download_nltk_data_if_needed(packages):
    for package in packages:
        try:
            nltk.data.find(package)
        except LookupError:
            nltk.download(package.split("/")[-1])

# Specify the NLTK data you need
required_nltk_packages = [
    'tokenizers/punkt',
    'corpora/wordnet',
    'corpora/stopwords'
]

# Call the function to download data if needed
download_nltk_data_if_needed(required_nltk_packages)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def remove_html_tags(text):
    # Remove html tags from a string
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def tokenize(text):
    # Tokenize text
    return word_tokenize(text)

def remove_stopwords(tokens):
    # Remove stopwords from a list of tokens
    return [i for i in tokens if not i.lower() in stop_words]

def lemmatize(tokens):
    # Lemmatize a list of tokens
    return [lemmatizer.lemmatize(token) for token in tokens]

def preprocess_text(text):
    # Main function to clean and preprocess text
    text = remove_html_tags(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize(tokens)
    return ' '.join(tokens)
