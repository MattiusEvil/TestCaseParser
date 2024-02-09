import scrapy


class NyhockeySpider(scrapy.Spider):
    name = "NYHockey"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["http://www.scrapethissite.com/pages/forms/"]
    _posted_form ={
        'q':"New York",
    }

    def start_requests(self):
        '''
        Отправляем POST запрос,
        содержащий форму New York

        В ответ получаем response,
        который обрабатывает parse
        '''
        return [
        scrapy.FormRequest(
            url=self.start_urls[0],
            formdata=self._posted_form,
            callback=self.parse,
        )
        ] 

    def parse(self, response):
        '''
        Итерируемся по командам
        и сохраняем статистику 
        в post.json
        '''
        if response.status:
            for i in range(len(response.xpath('//td[@class="name"]/text()').extract())):
                yield {
            'Team Name':response.xpath('//td[@class="name"]/text()').extract()[i].strip(),
            'Year':response.xpath('//td[@class="year"]/text()').extract()[i].strip(),
            'Wins':response.xpath('//td[@class="wins"]/text()').extract()[i].strip(),
            'Losses':response.xpath('//td[@class="losses"]/text()').extract()[i].strip(),
            'Ot_Losses':response.xpath('//td[@class="ot-losses"]/text()').extract()[i].strip(),
            'WinPer':response.xpath('//td[@class="pct text-success"]/text()').extract()[i].strip(),
            'GF':response.xpath('//td[@class="gf"]/text()').extract()[i].strip(),
            'GA':response.xpath('//td[@class="ga"]/text()').extract()[i].strip(),
            'Distinction':response.xpath('//td[@class="diff text-success"]/text()').extract()[i].strip(),
            }

