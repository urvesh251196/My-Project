#Importing all the necessary files
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import HKF

def logic(product,budget):

    #defining necessary variables
    page=1
    i=1
    max_pages=1

    #defining path and standard url pattern
    path='D:/urvesh/Project/Program/2.csv'
    url='https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page='+str(page)+'&q='+str(product)+'&viewType=grid'

    #scraping url into text format    
    source_code=requests.get(url)
    text=source_code.text
    soup=BeautifulSoup(text,'lxml')

    #for finding no. of pages each search may consist
    for max_p in soup.findAll(['span','a'], {'class': "_3v8VuN"}):
        pages=max_p.text
        p=word_tokenize(pages)
        p1=str(p[-1])
        max_pages=int(p1.replace(',',''))

    #main loop starts
    while page<=max_pages:

        #printing oage no. and incrementing page no. 
        print('Page no.: ' + str(page))
        url='https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page='+str(page)+'&q='+product+'&viewType=grid'
        page+=1

        #scraping url
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')

        #outer loop for finding products
        for prod_details in soup.findAll('div',{'class':'_3liAhj'}):
##            for img in prod_details.findAll('img',{'class' : '_1Nyybr _30XEf0'}):  
####                image=img.get('src')
##
            #this loop extracts titles and links from the web page
            for details in prod_details.findAll('a',{'class' : '_2cLu-l'}):

                title=details.get('title')
                link=details.get('href')
                link='https://www.flipkart.com' + str(link)

                #this loop is extracts all types of price details in the web page
                for price in prod_details.findAll('div',{'class' : '_1uv9Cb'}):
                    for dp in price.findAll('div',{'class' : ['_1vC4OE','_1vC4OE _2rQ-NK']}):
                            #replacing unnecessary things from deal_price like rupee symbol and comma
                            deal_price=int(dp.text.replace(u'\u20b9','').replace(',',''))

                            #checking necessary condition
                            if(deal_price <= budget):

                                for np in price.findAll('div',{'class' : '_3auQ3N'}):
                                    for dis in price.findAll('div',{'class' : 'VGWI6T'}):

                                        #replacing unnecessary things from norm_price like rupee symbol and comma
                                        norm_price=np.text.replace(u'\u20b9','').replace(',','')
                                        ##replacing unnecessary things from discount like off and %
                                        discount=word_tokenize(dis.text)
                                        discount=discount[0]

                                        #printing everything
                                        print('\nProduct id :' + str(i))
                                        print('Name of the product : ' + title)
                                        print('Discount : '+ str(discount) +'%')     
                                        print('Deal Price : Rs. ' + str(deal_price))
                                        print('Normal Price : Rs. ' + str(norm_price))
                                        print('Product link : '+ link+'\n')

                                        #merging every variable and converting into excel sheet (.csv format)
                                        info=str(str(i)+','+str(title)+','+str(deal_price)+','+str(norm_price)+',')
                                        HKF.write_file(path,link,info)

                                        #Incrementing product id
                                        i+=1
                            else:
                            #do nothing
                               pass
