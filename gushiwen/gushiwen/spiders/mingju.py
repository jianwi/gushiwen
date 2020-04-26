# -*- coding: utf-8 -*-
import scrapy
from ..items import GushiwenItem

class MingjuSpider(scrapy.Spider):
    name = 'mingju'
    allowed_domains = ['so.gushiwen.org']
    start_urls = ['https://so.gushiwen.org/mingju/default.aspx?p=1&c=&t=']

    def parse(self, response):
        for cont in response.xpath("//div[@class='left']/div[@class='sons']/div[@class='cont']"):
            sentence = cont.xpath("./a[1]/text()").extract()[0]
            title = cont.xpath("./a[2]/text()").extract()[0]

            juzi = GushiwenItem()
            juzi['sentence'] = sentence
            juzi['title'] = title

            yield juzi
        next_page = response.xpath("//a[@class='amore']/@href").extract()[0]
        if next_page:
            url = 'https://so.gushiwen.org'+next_page
            print(url)
            yield scrapy.Request(url, callback=self.parse)

