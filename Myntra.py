import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF


def logic(name):

    page=1
    max_pages=2
    product_link='https://www.myntra.com/web/v2/search/data/'+str(name)+'?f=&p='+str(page)+'&rows=48'
    
    while page<=max_pages:

        product_link='https://www.myntra.com/web/v2/search/data/'+str(name)+'?f=&p='+str(page)+'&rows=48'
        page+=1
        
        source_code=requests.get(product_link)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')

        print(soup)


name='shirts'
logic(name)
    
        
