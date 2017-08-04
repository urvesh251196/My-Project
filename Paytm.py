import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF

def logic(max_pages):
    page=2
    i=1
    path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
    if page<=max_pages:
        url='https://paytm.com/shop/g/watches?src=1&q=watches'
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
                if(deal>=80 & deal<=90):
                    print(i)
                    i+=1
                    print(deal)
                    
                    print('https://paytmmall.com'+link)
                    HKF.write_file(path,link,info)
                else:
                    pass        