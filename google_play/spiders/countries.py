import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['url']
    start_urls = ['http://url/']

    def parse(self, response):
        pass
