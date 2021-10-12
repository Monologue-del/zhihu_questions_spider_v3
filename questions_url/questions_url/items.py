# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionsUrlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    question_createdTime = scrapy.Field()
    answer_count = scrapy.Field()
    follower_count = scrapy.Field()
    comment_count = scrapy.Field()
    author_id = scrapy.Field()
    author_type = scrapy.Field()
    author_url = scrapy.Field()
    author_name = scrapy.Field()
    author_is_org = scrapy.Field()
