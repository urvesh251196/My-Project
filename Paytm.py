import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF

def logic(product ,max_pages, discount):
    page=2
    i=1
    if page<=max_pages:
        url='https://paytm.com/shop/g/' + product + '?src=1&q=' + product
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
        for item in soup.findAll('a',{'class':'_8vVO'}):
            link=item.get('href')
            for cond in item.findAll('span',{'class' : 'c-ax'}):
                cond1=word_tokenize(cond.text)
                deal1=str(cond1[0]).replace('-','')
                deal=int(deal1)

                info=str(str(i)+','+str(deal)+',')
                if(deal >= discount):
                    print("Product no. " + str(i))
                    i+=1
                    print("Deal price " + str(deal))
                    
                    print('Product Link : https://paytmmall.com'+link)
                    HKF.write_file(link,info)
                else:
                    pass        
