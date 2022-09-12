import scrapy
import logging


class AppsSpider(scrapy.Spider):
    name = 'apps'
    allowed_domains = ['play.google.com']
    start_urls = [
        'https://play.google.com/store/apps/details?id=com.Kiroogames.AurionKGF/']

    def parse(self, response):
        title = response.xpath(
            "//h1[@class='AHFaub']/span/text()").get(default=None)
        editor = response.xpath(
            "//a[@class='hrTbp R8zArc']/text()").get(default=None)
        grade = response.xpath(
            "//div[@class='K9wGie']/div[@class='BHMmbe']/text()").get()
        reviews = response.xpath(
            "//span[@class='AYi5wd TBRnV']/span[1]/text()").get()
        five_stars_perc = response.xpath(
            "//span[@class='L2o20d P41RMc']/@style").get()
        four_stars_perc = response.xpath(
            "//span[@class='L2o20d tpbQF']/@style").get()
        three_stars_perc = response.xpath(
            "//span[@class='L2o20d Sthl9e']/@style").get()
        two_stars_perc = response.xpath(
            "//span[@class='L2o20d rhCabb']/@style").get()
        one_stars_perc = response.xpath(
            "//span[@class='L2o20d A3ihhc']/@style").get()
        additional_info = response.xpath(
            "//div[@class='IxB2fe']/span[@class='htlgb']").get()
        additional_info = response.xpath(
            "//div[@class='IQ1z0d']/span[@class='htlgb']").getall()

        # yield scrapy.Request(url=link)
        yield
        {
            'title': title,
            'editor': editor,
            'grade': grade,
            'reviews': reviews,
            'five_stars_perc': five_stars_perc,
            'four_stars_perc': four_stars_perc,
            'three_stars_perc': three_stars_perc,
            'two_stars_perc': two_stars_perc,
            'one_stars_perc': one_stars_perc,
            'additional_info': additional_info
        }
