from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import pandas as pd

LIMIT = 3

def calculating(sample):
    
    sample = str(sample)
    
    if len(sample) <= LIMIT:
        return "Invalid!"
    
    tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

    tokens = tokenizer.encode(sample, return_tensors="pt")
    result = model(tokens)
    rated_result = int(torch.argmax(result.logits))
    
    ratings = ["Very Bad☹️","Bad🙁","Meh😐","Good🙂","Very Good😃"]
    
    for count, i in enumerate(ratings):
        if rated_result == count:
            return ratings[count]
