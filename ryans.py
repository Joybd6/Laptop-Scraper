import scrapy
from Items import Laptop

class TestScrapping(scrapy.Spider):
    name = 'test_scrapping'
    start_urls = [f"https://www.ryanscomputers.com/category/laptop-all-laptop"]
    page_number = 1
    page_limit = 75

    def parse(self, response):
        for data in response.css('.card-body.text-center'):
            item = Laptop()
            item['name'] = data.css('p>a').attrib['title']
            item['price'] = data.css('.pr-text::text').get()
            item['reseller'] = 'Ryans Computers'
            item['url'] = data.css('p>a').attrib['href']

            yield item
        
        self.page_number += 1

        next_page = f"https://www.ryanscomputers.com/category/laptop-all-laptop?page={self.page_number}"

        if self.page_number <= self.page_limit:
            yield response.follow(next_page, callback = self.parse)

