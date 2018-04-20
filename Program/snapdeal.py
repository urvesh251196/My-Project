import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import HKF

def snapdeal(name,budget):

    page=0
    i=1
    pid = 1
    url='https://www.snapdeal.com/acors/json/product/get/search/0/'+str(page)+'/20?q=&sort=rlvncy&brandPageUrl=&keyword='+str(name)+'&searchState=previousRequest=true|serviceabilityUsed=false|filterState=null&pincode=&vc=&webpageName=searchResult&campaignId=&brandName=&isMC=false&clickSrc=go_header&cartId=&page=srp'

    link=requests.get(url)
    text=link.text
    soup=BeautifulSoup(text,'lxml')


    for mpage in soup.find('div',{'class' :'jsNumberFound hidden'}):
        max_page = int(mpage)
        print max_page
        
    while(page <= max_page):

        url='https://www.snapdeal.com/acors/json/product/get/search/0/'+str(page)+'/20?q=&sort=rlvncy&brandPageUrl=&keyword='+str(name)+'&searchState=previousRequest=true|serviceabilityUsed=false|filterState=null&pincode=&vc=&webpageName=searchResult&campaignId=&brandName=&isMC=false&clickSrc=go_header&cartId=&page=srp'

        link=requests.get(url)
        text=link.text
        soup=BeautifulSoup(text,'lxml')

        print 'Page no. : ' + str(i) + '\n'
        
        i+=1
        page+=20

        for loop in soup.findAll('div',{'class' : 'product-desc-rating '}):
            for dp in loop.findAll('span',{'class' : 'lfloat product-price'}):
                deal_price=int(dp.get('data-price'))

                if(deal_price <= budget):

                    for links in loop.findAll('a',{'class' :'dp-widget-link noUdLine'}):
                        link = str(links.get('href'))

                        for t in loop.findAll('p',{'class' :'product-title '}):
                            title=str(t.get('title'))

                            for np in loop.findAll('span',{'class' :'lfloat product-desc-price strike '}):
                                np = word_tokenize(np.text.replace(',',''))
                                norm_price = np[-1]

                                print str(pid) +'.  ' + title
                                print deal_price
                                print norm_price
                                print link + str('\n')

                                info=str(str(pid)+','+str(title)+','+str(deal_price)+','+str(norm_price)+',')
                                HKF.write_file(link,info)
                                
                                pid+=1

                            
