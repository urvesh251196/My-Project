import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF
 
 
def logic(max_pages):
    
    page=1
    result=[]
    i=1
    path='D:\urvesh\Project\Program\1.csv'
    product=raw_input("Enter product name : ")
    
    while page<=max_pages:
        
##        print('Page no.: ' + str(page))
        url='https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page='+str(page)+'&q='+product+'&viewType=grid'
        page+=1
        

        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')

        for max_p in soup.findAll('span',{'class' : {'_3v8VuN'}}):
            pages=max_p.text
            p=word_tokenize(pages)
            p1=str(p[-1])
            print(p1.replace(',',''))


logic(1)
