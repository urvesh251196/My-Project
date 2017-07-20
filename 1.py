import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
#import decimal

def flipkart(max_pages):
    page=3
    result=[]
    i=1
    path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
    while page<=max_pages:
        url='https://www.flipkart.com/books/educational-and-professional-books/pr?otracker=categorytree&page='+str(page)+'&q=books&sid=bks%2Cenp&viewType=grid'
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
                if(result>=60):
                    print(i)
                    i+=1
                    print(result)
                    links='https://www.flipkart.com'+link
                    print(links)
                    write_file(path,links,info)
                else:
                    pass
                    
def paytm(max_pages):
    page=3
    result=[]
    i=1
    path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
    if page<=max_pages:
        url='https://paytmmall.com/shop/search?q=red%20tape&from=organic&child_site_id=6&site_id=2'
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
        for item in soup.findAll('a',{'class':'_8vVO'}):
            link=item.get('href')
            for cond in item.findAll('div',{'class' : '_27VV'}):
                cond1=word_tokenize(cond.text)
                result=str(cond1[0]).replace('WOW','0').replace('BEST','0').replace('Must','0')
                #deal1=str(result)
                deal=int(result)
                #info=str(str(i)+','+str(result)+',')
                if(deal>=10):
                    print(i)
                    i+=1
                    print(deal)
                    
                    print(link)
                    #write_file(path,links,info)
                else:
                    pass                   

#def amazon(max_pages):
#    page=2
#    result=[]
#    i=1
#    path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
#    #D=decimal.Decimal
#   # while page<=max_pages:
#    url='http://www.amazon.in/s/ref=sr_pg_1?fst=as%3Aoff&rh=n%3A1350387031%2Cn%3A%211499791031%2Cn%3A%211499793031%2Cn%3A5522778031%2Cp_98%3A10440597031%2Cp_6%3AA33OPBN6TQ5DP7%2Cp_n_pct-off-with-tax%3A2665401031&bbn=5522778031&ie=UTF8&qid=1500459752'
#        #page+=1
#    source_code=requests.get(url)
#    text=source_code.text
#    soup=BeautifulSoup(text,'lxml')
#    for item in soup.findAll('a',{'class':'a-link-normal a-text-normal'}):
#        link=item.get('href')
#        for deal_price in item.findAll('span',{'class' : 'a-size-base a-color-price s-price a-text-bold'}):
#            cond1=float(u'deal_price.text')
#            #result=str(cond1[0])
#            #cond=str(cond1)
#            cond=int(cond1)
#            print(cond)
#            #info=str(result)
#            #if(result>=70):
#            #    print(i)
#            #    i+=1
#            #    print(result)
#            #    links='https://www.flipkart.com'+link
#            #    print(links)
#            #    write_file(path,links,info)
#            #else:
#            #    pass
#            #        
#            #
#                    
                    
def write_file(path, data, info):
    with open(path, 'a') as f:
        #f.write(index_no)
        #f.write(dis+'\n')
        f.write(info)
        f.write(data+'\n')
                    
flipkart(361)
#amazon(50)
paytm(3)