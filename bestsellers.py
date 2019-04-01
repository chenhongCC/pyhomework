import scrapy
import bs4
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name='dangdang'
    allowed_domains=['http://bang.dangdang.com']
    start_urls = []
    for i in range(3):
        url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-'+str(i+1)
        start_urls.append(url)
        
    def parse(self,response):
        book_bs=bs4.BeautifulSoup(response.text,'html.parser')
        books=book_bs.find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
        for book in books:
            item=DangdangItem()
            item['name']=book.find('div',class_='name').find('a')['title']
            item['author']=book.find('div',class_='publisher_info').find('a')['title']
            item['price']=book.find('div',class_='price').find('span',class_='price_n').text
            print(item['name'],item['author'],item['price'])
            yield item