import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast
import pandas as pd
import numpy
import time
import pickle

df = pd.read_pickle("corpus.pkl") # insert a correct path
texts = df['text']

from transformers import AutoTokenizer, AutoModelForSequenceClassification
model_checkpoint = 'cointegrated/rubert-tiny-sentiment-balanced'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)

def get_sentiment(text, return_type='label'):
    """ Calculate sentiment of a text. `return_type` can be 'label', 'score' or 'proba' """
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(model.device)
        proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()[0]
    if return_type == 'label':
        return model.config.id2label[proba.argmax()]
    elif return_type == 'score':
        return proba.dot([-1, 0, 1])
    return proba

# Classify the text

labels = [get_sentiment(i, 'label') for i in texts]

# Score the text on the scale from -1 (very negative) to +1 (very positive)

score = [get_sentiment(i, 'score') for i in texts]
# calculate probabilities of all labels
predictions1 = [get_sentiment(i, 'proba')[0] for i in texts]
predictions2 = [get_sentiment(i, 'proba')[1] for i in texts]
predictions3 = [get_sentiment(i, 'proba')[2] for i in texts]

df['labels'] = labels
df['score'] = score

# Save an updated dataframe
df.to_pickle( ) # insert a correct path

