import scrapy
from itemadapter import ItemAdapter

class Laptop(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    reseller = scrapy.Field()
    url = scrapy.Field()