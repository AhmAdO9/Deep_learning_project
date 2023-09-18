from bs4 import BeautifulSoup
import requests
import nltk
from tqdm import tqdm,trange
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path
import csv
import  openpyxl
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
from transformers import AutoTokenizer

# si = SentimentIntensityAnalyzer()
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


def polarity_scores_roberta(example):
    encoded_text = tokenizer(example,padding='max_length', truncation=True, max_length=100000)
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
    'roberta_neg':scores[0],
    'roberta_neu':scores[1],
    'roberta_pos':scores[2]
}
    return scores_dict

file = openpyxl.load_workbook("Input.xlsx")
activated = file.active
data = []
f = open("doc.csv", "w")
writer = csv.writer(f)
for i in tqdm(activated, ncols=100):
    if i[1].value == 'URL':
            continue
    else:
        response = requests.get(i[1].value)
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.select("div[class='td-post-content tagdiv-type'] p")
        collected = ''
        for i in (content):
            collected = collected + i.text
        try:
            data.append(polarity_scores_roberta(collected))
        except RuntimeError:
             print("error")
        
# print(data)

for i in data:
    writer.writerow(i.values())                      

f.close()
file.close()