import scrapy
import json


class FilmspiderSpider(scrapy.Spider):
    name = "filmspider"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript"]

    def start_requests(self):
        pages = [pages for pages in range(2010, 2015 + 1)]
        '''
        Внесем в метод start_requests итерацию 
        по ссылкам на списки фильмов по годам 
        для парсинга всей страницы. 
        ''' 
        for page in pages:
            url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={page}"
            yield scrapy.Request(url=url, callback=self.parse)
        '''
        Данные по фильмам передаются
        на сайт динамически после проверки 
        сервером, по этому обращаемся
        к внешнему json ресурсу. 
        ''' 

    def parse(self, response, **kwargs):
        items = json.loads(response.text) #Выгружаем json с сайта в films.json
        for item in items: yield item
        
