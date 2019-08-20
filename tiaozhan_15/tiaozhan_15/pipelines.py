# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Tiaozhan15Pipeline(object):
    def open_spider(self,spider):
        spider.file = open('spider_tiaozhan','w',encoding='utf-8')
        print('爬虫开始了。')

    def process_item(self, item, spider):
        line = '{}.\n'.format(json.dumps(dict(item)))
        self.file.write(line)

    def close_spider(self,spider):
        spider.file.close()
        print('爬虫结束了')