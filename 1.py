import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords

def web_spider(max_pages):
    page=2
    result=[]
    i=1
    #stop_words=set(stopwords.words("english"))
    while page<=max_pages:
        url='https://www.flipkart.com/mens-footwear/pr?otracker=nmenu_sub_Men_0_Footwear&page='+str(page)+'&sid=osp%2Ccil&viewType=grid'
        page+=1
        source_code=requests.get(url)
        text=source_code.text
        soup=BeautifulSoup(text,'lxml')
        for item in soup.findAll('a',{'class':'_1Vfi6u'}):
            link=item.get('href')
            for cond in item.findAll('div',{'class' : 'VGWI6T _14zQzR'}):
                cond1=word_tokenize(cond.text)
                result=int(cond1[0])
                if(result>=10):
                    print(i)
                    i+=1
                    print(result)
                    print('https://www.flipkart.com'+link)
                else:
                    pass
     
result=web_spider(20)
#print(result)