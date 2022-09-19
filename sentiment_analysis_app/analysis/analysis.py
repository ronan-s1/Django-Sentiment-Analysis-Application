from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import io
import urllib, base64
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#constants
SENTIMENTS = ["Very Bad☹️","Bad🙁","Meh😐","Good🙂","Very Good😃"]
TOKENIZER = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
MODEL = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

#calculating sentiment
def calculating(sample):
    
    #initiating model
    tokens = TOKENIZER.encode(sample, return_tensors="pt")
    result = MODEL(tokens)
    rated_result = int(torch.argmax(result.logits))
    
    #matching sentiment score with words
    for count, i in enumerate(SENTIMENTS):
        if rated_result == count:
            return SENTIMENTS[count]

#getting sentiment of yelp reviews
def yelp(url):
    #scrapping and cleaning text from yelp page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    regex = re.compile(".*comment.*")
    results = soup.find_all("p", {"class": regex})
    reviews = [result.text for result in results]
    
    #putting reviews in a dataframe and calculating each review's sentiment
    df = pd.DataFrame(np.array(reviews), columns=["review"])
    df["sentiment"] = df["review"].apply(lambda x: calculating(x[:512]))

    #seeing how many reviews have each score of sentiment
    sentiment_amount = [df["sentiment"].loc[df["sentiment"] == SENTIMENTS[i]].size for i in range(len(SENTIMENTS))]
    
    
    #plotting graph, using AGG to allow running outside main thread
    matplotlib.use("Agg")
    plt.bar(["Very Bad","Bad","Meh","Good","Very Good"], sentiment_amount, color=("green"))
    plt.title("Reviews")
    plt.xlabel("Sentiment levels")
    plt.ylabel("Reviews")
    plt.tight_layout()
    fig = plt.gcf()
    
    #converting graph into dtring buffer
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    
    #converting 64 bit code into image
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    
    review_short = [review[:512] + "..." if len(review) > 512 else review for review in reviews]
    return [uri, review_short, df.sentiment.values.tolist()]
