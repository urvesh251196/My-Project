import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF


def logic(max_pages):
    page=1
    #i=1
    product_link='https://www.myntra.com'
    #path=os.path.join('D:/urvesh/Desktop/Urvesh/1.csv')
    while page<=max_pages:
        
        page+=1
        source_code=requests.get(product_link)
        text=source_code.text
        print(text)
        soup=BeautifulSoup(text,'lxml')
        
    
        
        #path='D:urvesh/Desktop/Urvesh/2.csv'
        ##with open(path,'a') as f:
        ##    f.write(soup)
        #for item in soup.findAll('li',{'class':'product-base'}):
        #    print(item)
        for link in soup.findAll('a'):
            pro_link=link.get('href')
            print(pro_link)
        #    #print('www.myntra.com'+str(pro_link))
        #    with open(path,'a') as f:
        #        f.write(str(pro_link))
        #print("done")
            #    print(pro_link)
            #    for cond in link.findAll('span',{'class' : 'product-discountPercentage'}):
            #        print(cond)
                    #cond1=word_tokenize(cond.text)
                    #result=int(cond1[0])
                    #info=str(str(i)+','+str(result)+',')
                    #if(result>=50):
                    #    print(i)
                    #    i+=1
                    #    print(result)
                    #    links='https://www.flipkart.com'+link
                    #    print(links)
                    #    #write_file(path,links,info)
                    #else:
                    #    pass
                    #