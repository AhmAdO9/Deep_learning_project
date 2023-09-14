from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

topic = list(open("topics.csv","r", encoding="utf-8"))
article = list(open("articles.csv","r",encoding="utf-8"))
for b in range(0,30):
    browser = webdriver.Chrome()
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdrKj0TsGxNY1Hfks2Y8QyW4K-Xr4IW4Yvd23lxTCmqyivDEQ/viewform")
    browser.maximize_window()
    browser.implicitly_wait(3)
    s = browser.find_elements(By.CSS_SELECTOR,'input[type="text"]')
    s1 = browser.find_elements(By.CSS_SELECTOR,'textarea[class="KHxj8b tL9Q4c"]')
    s2 = browser.find_elements(By.CSS_SELECTOR,'input[type="date"]')
    j=1
    k=0
    n=0
    m=3
    l=0
    for i in s:
        if j>3 :
            j=2
        if j % 3 == 0:
            k+=1
        data = ["Faheem Ahmad", "Times of India", topic[k-1]]
        i.send_keys(data[j-1])
        if n <= 2:
            if b > 21:
                s2[n].send_keys("10-01-2014")
            else:
                s2[n].send_keys("01-01-2014")
            s1[n].send_keys(article[n])
            n+=1
        if m <=5 and l <=2 :
            s1[m].send_keys(f"{article[l][:400]}...")
            m+=1
            l+=1
        j+=1
    for i in range(0,3):
        article.pop(0)
        topic.pop(0)
    
    
    
    # browser.find_element(By.XPATH,'//span[@class="l4V7wb Fxmcue"] //span[text()="Submit"]').click()
        

