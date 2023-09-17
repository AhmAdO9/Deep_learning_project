import os
import openai
from tqdm import tqdm


openai.api_key = "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"

    
def get_completion(prompt, model="gpt-3.5-turbo"):


    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

    )

    return response["choices"][0]["message"]["content"]


file = open("articles.csv","r",encoding="utf-8")
file1 = open("summary.csv","a", encoding="utf-8")


for i in tqdm(file, ncols=100):
    prompt = f'''write a summary of the article provided in not more than 50 words is a must: {{{i}}}'''
 
    response = get_completion(prompt)
    file1.write(response)
    file1.write("\n")
    


