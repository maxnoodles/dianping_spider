# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    mail_id = scrapy.Field()
    mail_regionName = scrapy.Field()
    shop_id = scrapy.Field()
    shop_name = scrapy.Field()
    shop_url = scrapy.Field()
    shop_address = scrapy.Field()


