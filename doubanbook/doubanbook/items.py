# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price =scrapy.Field()
    publisher = scrapy.Field()
   
    edition = scrapy.Field()
    author =scrapy.Field()
    pass
class CaoItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()
    industry = scrapy.Field()