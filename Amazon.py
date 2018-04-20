##Problems:
##
##    Junk values of price1 and price2
##    max_pages = unknown  
##    wrong loops choosen



import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF

def amazon(product,budget):

    pages=1
    max_pages=1

    base_url='http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+str(product)+'&rh=i%3Aaps%2Ck%3A'+str(product)

    while pages<=max_pages:    

##        url='http://www.amazon.in/'+str(product_name)+'/s?ie=UTF8&page='+str(pages)+'&rh=i%3Aaps%2Ck%3A'+str(product_name)
        
        source_code=requests.get(base_url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
            
        print('\nPage no. : ' + str(pages))
        print(base_url)
        pages+=1
        

        nextpage(soup,base_url,max_pages,pages)
##
##        deal_price(soup,budget)
##
##
##def deal_price(soup,budget):
##    
##    for deal_price in soup.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
##        link1=deal_price.text.replace(',','')
##        tokenize1=word_tokenize(link1)
##        price1=int(tokenize1[0])
##        
##        title(soup,price1,budget)
##
##
####def org_price(soup,price1,budget):
####
####    for org_price in soup.findAll('span',{'class':'a-size-small a-color-secondary a-text-strike'}):
####
####        link2=org_price.text.replace(',','')
####        tokenize2=word_tokenize(link2)
####        price2=int(tokenize2[0])
####        print(price2)
####        title(soup,price1,price2,budget)
####
##def title(soup,price1,budget):
##
##    for details in soup.findAll('a',{'class' : 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}):
##                    
##         if(price1<=budget):    
##            title=details.text.encode('UTF-8')
##            link=str(details.get('href'))
##            print('\nProduct name : ' + str(title))
##            print('Deal Price= '+str(price1))
##            print('Link = ' +str(link))
##         else:
##            pass      
                    
def nextpage(soup,base_url,max_pages,pages):

        for a in soup.findAll('span',{'class' : {'pagnLink'}}):

            max_pages=int(a.text)
            if(pages==max_pages):
                for page in a.findAll('a'):
                    page_link=page.get('href')
                    base_url=page_link
                
                    print('http://www.amazon.in'+str(base_url))
                    print(max_pages)
                    max_pages+=1
            else:
                max_pages+=1


            
      
                         
                    
##                    
##                    if(price1 != 0 and price2!=0):
##                        print("i'm in if loop")
##                        results=0
##                        results=100-((price1/price2)*100)
##                        print(results)
####                        
####                    
##                    
####
####

