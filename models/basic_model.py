import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn import functional as F
import torch.nn as nn

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

class Lambda(nn.Module):
    def __init__(self, func):
        super(Lambda, self).__init__()
        self.func = func

    def forward(self, x):
        return self.func(x)


class ModifiedBertForBiasDetection(BertForSequenceClassification):
    def __init__(self, config):
        super(ModifiedBertForBiasDetection, self).__init__(config)
        
        # Add a linear transformation layer after the classifier
        self.transformation = nn.Linear(config.num_labels, 1)
        
        # Apply a sigmoid activation (to get values between 0 and 1) and scale to 0-500
        self.activation = nn.Sequential(
            nn.Sigmoid(),
            Lambda(lambda x: x * 500)
        )

    def forward(self, input_ids, token_type_ids=None, attention_mask=None, labels=None):
        outputs = super().forward(input_ids, token_type_ids, attention_mask)
        
        # Pass the logits through the transformation layer
        logits = self.transformation(outputs.logits)
        
        # Apply the activation
        scaled_logits = self.activation(logits)
        
        return scaled_logits

# Instantiate the modified model
model = ModifiedBertForBiasDetection.from_pretrained(MODEL_NAME)


def predict_sentiment(text):
    # Predict sentiment of a piece of text using the modified BERT model.
    
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
        predicted_value = outputs[0].item()  # Get the scaled value

    return predicted_value
