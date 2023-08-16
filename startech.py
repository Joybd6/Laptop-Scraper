import scrapy
from Items import Laptop

class StarTechLaptop(scrapy.Spider):
    name = 'test_scrapping'
    start_urls = [f"https://www.startech.com.bd/laptop-notebook"]
    page_number = 1
    page_limit = 34
    def parse(self, response):
        for data in response.css('.p-item-details'):
            item = Laptop()
            item['name'] = data.css('h4>a::text').get()
            item['price'] = data.css('div>span::text').get()
            item['reseller'] = 'Startech'
            item['url'] = data.css('h4>a').attrib['href']

            yield item
        
        self.page_number += 1

        next_page = f"https://www.startech.com.bd/laptop-notebook?page={self.page_number}"

        if self.page_number <= self.page_limit:
            yield response.follow(next_page, callback = self.parse)







