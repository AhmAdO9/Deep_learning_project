from bs4 import BeautifulSoup
import requests
from pathlib import Path
import csv

# sites = ['india/g20-summit','india']
# for i in sites:
url = "https://timesofindia.indiatimes.com/2014/10/1/archivelist/year-2014,month-10,starttime-41913.cms"
response = requests.get(url)
print(url)
soup = BeautifulSoup(response.text, "html.parser")
r = list(soup.find_all('span', style="font-family:arial ;font-size:12;color: #006699"))
sett = r[1].find_all('a')
j = 1
sp = -1
article = open(f"a.csv", "w", encoding="utf-8")
topic = open(f"t.csv", "w", encoding="utf-8")
for  i in sett:
    try:
        if j <=40:
            url = f"{i.get('href')}"
            # print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            head= soup.select_one('h1[class="HNMDR"]')
            body = soup.select_one('div[data-articlebody="1"] > section').next_sibling
            topic.write(head.text)
            topic.write("\n")
            article.write(body.text)
            article.write("\n")
            j+=1
        else:
            break
    except (
AssertionError,	
AttributeError,
EOFError,
FloatingPointError,	
GeneratorExit,
ImportError,	
IndexError,
KeyError,
KeyboardInterrupt,
MemoryError,
NameError,
NotImplementedError,
OSError,
OverflowError,
ReferenceError,
RuntimeError,
StopIteration,
SyntaxError,
IndentationError,
TabError,
SystemError,
SystemExit,
TypeError,
UnboundLocalError,
UnicodeError,
UnicodeEncodeError,
UnicodeDecodeError,
UnicodeTranslateError,
ValueError,
ZeroDivisionError
):
     j+=1
        
