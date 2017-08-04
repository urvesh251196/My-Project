import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os

def flipkart(max_pages):
        
        page=1
        product=raw_input("Enter products name : ")
        while page<=max_pages:
            url='https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page='+str(page)+'&q='+product+'&viewType=grid'
            page+=1
            print(url)
        
        
        
        #source_code=requests.get(url)
        #text=source_code.text
        #soup=BeautifulSoup(text,'lxml')
        
        
   
   
flipkart(10)