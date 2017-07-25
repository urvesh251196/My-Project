from __future__ import division
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os


def flipkart(max_pages):
    page=1
    result=[]
    i=1
    product_link='https://www.flipkart.com/search?q=smartphones&otracker=start&as-show=on&as=off'
    path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
    while page<=max_pages:
        if page==1:
            url=product_link
        else:
            url=product_link+str(page)+'&viewType=grid'
        print(page)
        page+=1
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
        for item in soup.findAll('a',{'class':'_1Vfi6u'}):
            link=item.get('href')
            for cond in item.findAll('div',{'class' : 'VGWI6T _14zQzR'}):
                cond1=word_tokenize(cond.text)
                result=int(cond1[0])
                info=str(str(i)+','+str(result)+',')
                if(result>=50):
                    print(i)
                    i+=1
                    print(result)
                    links='https://www.flipkart.com'+link
                    print(links)
                    write_file(path,links,info)
                else:
                    pass
                    
def paytm(max_pages):
    page=2
    result=[]
    i=1
    path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
    if page<=max_pages:
        url='https://paytmmall.com/shop/search?q=funk%20sunglasses&from=autosuggest&child_site_id=6&site_id=2'
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
        for item in soup.findAll('a',{'class':'_8vVO'}):
            link=item.get('href')
            for cond in item.findAll('div',{'class' : '_27VV'}):
                cond1=word_tokenize(cond.text)
                result=str(cond1[0]).replace('WOW','0').replace('BEST','0').replace('Must','0').replace('+','0').replace('International','0')
                #deal1=str(result)
                deal=int(result)
                #info=str(str(i)+','+str(result)+',')
                if(deal>=50):
                    print(i)
                    i+=1
                    print(deal)
                    
                    print('https://paytmmall.com'+link)
                    #write_file(path,links,info)
                else:
                    pass                   

def amazon(max_pages):
    page=3
    
    url='http://www.amazon.in/s/ref=sr_pg_2?fst=as%3Aon&rh=k%3Awatches%2Cn%3A1350387031&page='+str(page)+'&keywords=watches&ie=UTF8&qid=1500900573&spIA=B00RK5PFEY,B06XSJ1X95,B06XJGZJ6X'
    source_code=requests.get(url)
    text=source_code.text
    soup=BeautifulSoup(text,'lxml')
    while page<=max_pages:
        print(page)
        page+=1
        for cost_price in soup.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
            link1=cost_price.text.replace(',','')
            tokenize1=word_tokenize(link1)
            price1=int(tokenize1[0])
            print('price1= '+str(price1))
            
        for org_price in soup.findAll('span',{'class':'a-size-small a-color-secondary a-text-strike'}):
            link2=org_price.text.replace(',','')
            tokenize2=word_tokenize(link2)
            price2=int(tokenize2[0])
            print('price2= '+ str(price2))
        cond(price1,price2)
           
def cond(price1,price2):
    results=0
    results-=(price1/price2)*100
    print(results)                    
                    
def write_file(path, data, info):
    with open(path, 'a') as f:
        #f.write(index_no)
        #f.write(dis+'\n')
        f.write(info)
        f.write(data+'\n')
                    
#flipkart(208)
#amazon(10)
paytm(10)
