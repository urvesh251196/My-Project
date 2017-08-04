import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF
 
 
def logic():
    
    page=1
    result=[]
    i=1
    path='D:/urvesh/Project/Program/1.csv'
    product=raw_input("Enter product name : ")

    url='https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page=1&q='+product+'&viewType=grid'
    
    source_code=requests.get(url)
    text=source_code.text
    soup=BeautifulSoup(text,'lxml')

    for max_p in soup.findAll('span',{'class' : {'_3v8VuN'}}):
            pages=max_p.text
            p=word_tokenize(pages)
            p1=str(p[-1])
            max_pages=int(p1.replace(',',''))
            
            
 
    while page<=max_pages:
        
        print('Page no.: ' + str(page))
        url='https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page='+str(page)+'&q='+product+'&viewType=grid'
        page+=1
        

        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')

        

        for item in soup.findAll('a',{'class':'_1Vfi6u'}):
            link=item.get('href')
            for cond in item.findAll('div',{'class' : 'VGWI6T'}):
                cond1=word_tokenize(cond.text)
                result=int(cond1[0])
                info=str(str(i)+','+str(result)+',')
                if(result>=70):
                    print(i)
                    i+=1
                    print('Discount : '+ str(result) +'%')
                    links='https://www.flipkart.com'+link
                    print('Product link : '+ links)
                    HKF.write_file(path,links,info)
                else:
                   pass
