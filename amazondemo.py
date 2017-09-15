import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import os
import HKF

def a(product,budget):

    pages=1
    max_pages=1

##    base_url='http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+str(product)+'&rh=i%3Aaps%2Ck%3A'+str(product)
    base_url='https://www.amazon.in/titan-watches/s?ie=UTF8&page=7&rh=i%3Aaps%2Ck%3Atitan%20watches'

    while pages<=max_pages:
        
        source_code=requests.get(base_url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
        pages+=1
        
        print(soup)
        
        for npg in soup.findAll('span',{'class' : 'pagnRA'}):
            for link in npg.findAll('a',{'class': 'pagnNext'}):
                link=link.get('href')
                url='https://www.amazon.in' + str(link)
                base_url=url
                print(base_url)

                if(url):
                    max_pages+=1
                else:
                    pass

##
##    while pages<=max_pages:
##
##        source_code=requests.get(base_url)
##        text=source_code.text
##        soup=BeautifulSoup(text,'lxml')
##
##        print('\nPage no. : ' + str(pages))
##        print(base_url)
##        pages+=1
##
####        print(soup)
##        
####        for prod_details in soup.findAll('div',{'class' : 'a-fixed-left-grid-col a-col-right'}):
####            print(prod_details)
##        for details in soup.findAll('a',{'class' : 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}):
####                print(details)
##            title=details.get('title')
##            link=details.get('href')
##
##            for dp in soup.findAll('span',{'class' : ['a-size-base a-color-price s-price a-text-bold','a-size-base a-color-price a-text-bold']}):
####                    print(dp.text)
##                dp=word_tokenize(dp.text)
##                deal_price=int(dp[-1].replace(',',''))
##
##                if(budget >= deal_price):
####                        print('OK')
####                        for np in prod_details.findAll('span',{'class' : 'a-size-small a-color-secondary a-text-strike'}):
####                            print(np.text)
####                            np=word_tokenize(np.text)
####                            norm_price=int(np[-1].replace(',',''))
##
##                    print(title)
##                    print(deal_price)
####                            print(norm_price)
##                    print(link)
##
##                    for mp in soup.findAll('span',{'class' : 'pagnDisabled'}):
####                                print(mp.text)
##                        mp=int(mp.text)
##                        max_pages=mp
##
##                        for npg in soup.findAll('span',{'class' : 'pagnRA'}):
##                            for link in npg.findAll('a',{'class': 'pagnNext'}):
####                                    print(soup)
##                                link=link.get('href')
##                                base_url='https://www.amazon.in' + str(link)                       
##                else:
##                    pass
##        break
##
##    



product='titan+watches'
budget=2000
a(product,budget)
