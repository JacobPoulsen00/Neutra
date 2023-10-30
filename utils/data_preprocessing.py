import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

HTML_TAG_PATTERN = re.compile('<.*?>')

required_nltk_packages = [
    'tokenizers/punkt',
    'corpora/wordnet',
    'corpora/stopwords'
]

def download_nltk_data_if_needed(packages):
    """
    Download specified NLTK data packages if they aren't already present.
    """
    for package in packages:
        try:
            nltk.data.find(package)
        except LookupError:
            nltk.download(package.split("/")[-1])

download_nltk_data_if_needed(required_nltk_packages)
lemmatizer = WordNetLemmatizer()
stopword_set = set(stopwords.words('english'))

def remove_html_tags(text):
    """
    Remove HTML tags from a string.
    """
    return HTML_TAG_PATTERN.sub('', text)

def tokenize(text):
    """
    Tokenize text.
    """
    return word_tokenize(text)

def remove_stopwords(tokens, stopword_set):
    """
    Remove stopwords from a list of tokens.
    """
    return [token for token in tokens if token.lower() not in stopword_set]

def lemmatize(tokens, lemmatizer):
    """
    Lemmatize a list of tokens.
    """
    return [lemmatizer.lemmatize(token) for token in tokens]

def preprocess_text(text):
    """
    Main function to clean and preprocess text.
    """
    text = remove_html_tags(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens, stopword_set)
    tokens = lemmatize(tokens, lemmatizer)
    return ' '.join(tokens)