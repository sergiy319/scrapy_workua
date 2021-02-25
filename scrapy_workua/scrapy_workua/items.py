# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ScrapyWorkuaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# A class is created to define the structure of the fields.
class PeopleItem(Item):
    applicant_name = Field()
    applicant_old = Field()
    applicant_position = Field()
    detail_info = Field()
