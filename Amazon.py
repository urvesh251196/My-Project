import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF

def amazon(max_pages):
    
    page=2
    
    url='http://www.amazon.in/s/ref=sr_pg_2?fst=as%3Aon&rh=k%3Awatches%2Cn%3A1350387031&page='+str(page)+'&keywords=watches&ie=UTF8&qid=1500900573&spIA=B00RK5PFEY,B06XSJ1X95,B06XJGZJ6X'
    source_code=requests.get(url)
    text=source_code.text
    soup=BeautifulSoup(text,'lxml')
  
    while page<=max_pages:
        print(str(page)+'\n')
        page+=1
        
    for cost_price in soup.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
        link1=cost_price.text.replace(',','').replace('.00','')
        tokenize1=word_tokenize(link1)
        price1=int(tokenize1[0])
        print('price1= '+str(price1))            
        
        for org_price in soup.findAll('span',{'class':'a-size-small a-color-secondary a-text-strike'}):
           print()
           #     link2=org_price.text.replace(',','').replace('.00','')
           #     tokenize2=word_tokenize(link2)
           #     price2=int(tokenize2[0])
           #     print('price2= '+ str(price2))
           #     results=0
           #     results=100-((price1/price2)*100)
           #     print(results)      
           #