import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF

def logic():

    product_name=raw_input("Enter product name : ")
    max_pages=400
    page=1
    budget=input("Enter your budget : ")
    
    url='https://www.amazon.in/s/ref=sr_pg_2?fst=as%3Aon&rh=n%3A1350387031%2Ck%3A'+str(product_name)+'&page='+str(page)+'&keywords='+str(product_name)+'&ie=UTF8&qid=1502188451&spIA=B073QVBSJX,B00TZONN2O,B01DJ4G3ZE'
    source_code=requests.get(url)
    text=source_code.text
    soup=BeautifulSoup(text,'lxml')
  
    while page<=max_pages:
        print(str(page))
        page+=1
        
        for cost_price in soup.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
            link1=cost_price.text.replace(',','').replace('.00','')
            tokenize1=word_tokenize(link1)
            price1=float(tokenize1[0])
            if(price1<=budget):
                print('price1= '+str(price1)+'\n')
            else:
                pass
            
##            for org_price in soup.findAll('span',{'class':'a-size-small a-color-secondary a-text-strike'}):
##                link2=org_price.text.replace(',','').replace('.00','')
##                tokenize2=word_tokenize(link2)
##                price2=int(tokenize2[0])
##                print('price2= '+ str(price2))
            
        #     results=0
           #     results=100-((price1/price2)*100)
           #     print(results)      
           #
