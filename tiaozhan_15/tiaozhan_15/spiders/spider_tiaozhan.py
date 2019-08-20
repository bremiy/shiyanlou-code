# -*- coding: utf-8 -*-
import scrapy

from ..items import Tiaozhan15Item

class SpiderTiaozhanSpider(scrapy.Spider):
    name = 'spider_tiaozhan'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):

        rests = response.xpath('//*[@id="user-repositories-list"]')
        for rest in rests:


            name = rest.xpath('//h3//a/text()').getall()
            time = rest.xpath('//relative-time//@datetime').getall()
            print(name)
            print(time)

            #item = Tiaozhan15Item(name=name,time=time)
            #yield item
