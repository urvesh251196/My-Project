import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def snapdeal(product):

    url='https://www.snapdeal.com/search?keyword='+str(product)
    driver=webdriver.Chrome("C:\Python27\selenium\webdriver\chromedriver.exe")
    
    source_code=requests.get(url)
    text=source_code.text
    soup=BeautifulSoup(text,'lxml')

    logic(soup)


def logic(soup):
    
    for title in soup.findAll('p',{'class' : 'product-title '}):
        title =title.get('title')
        print(title)
        np(soup)


def np(soup):
    
    for np in soup.findAll('div',{'class' : 'see-more-products'}):
        driver.get(url)
        sbtn = driver.find_element_by_xpath('//*[@id="see-more-products"]')
        sbtn.click()
        driver.save_screenshot('snapdeal.png')
        driver.quit()
        logic(soup)

            
product_name='shirts'
snapdeal(product_name)
