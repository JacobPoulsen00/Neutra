import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForSequenceClassification.from_pretrained(MODEL_NAME)

SENTIMENT_MAPPING = {
    1: "Very Negative",
    2: "Negative",
    3: "Neutral",
    4: "Positive",
    5: "Very Positive"
}

def predict_sentiment(text):
    # Predict sentiment of a piece of text using a pretrained BERT model.
    
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        return_tensors="pt",
        padding='max_length',
        truncation=True
    )

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs[0]
        probabilities = softmax(logits, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item() + 1

    return SENTIMENT_MAPPING[predicted_class]