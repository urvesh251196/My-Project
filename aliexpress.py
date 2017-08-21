import requests
from bs4 import BeautifulSoup

def aliexpress():
    
    product_name=raw_input("Search for products... ")
    pages=1
    max_pages=2

    url='http://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20170821004256&SearchText='+str(product_name)

    while(pages<=max_pages):

        print("Page no. = " +str(pages))
        print("Page link = " + str(url))
        pages+=1

        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')

        print(soup)
        
        for page in soup.findAll('div',{'class' : 'ui-pagination-navi util-left'}):
                            
            for link in page.findAll('a',{'class' : 'page-next ui-pagination-next'}):

                print('Im inside the loop')
                url=link.get('href')
                max_pages=link.text
                url='https:' + str(url)
                print(url)
                break
        
        for product in soup.findAll('li',{'class' : ['list-item list-item-first ','list-item ']}):
            
            for info in product.findAll('div',{'class' : 'info'}):
                
                for details in info.findAll('a',{'class' : 'history-item product '}):
                    
                    link=details.get('href')
                    title=details.get('title')
                    print('\nName of the product : ' + str(title))
                    print('Product link :'+str(link)+'\n')

aliexpress()
