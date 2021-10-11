# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionsItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    detail = scrapy.Field()
    editableDetail = scrapy.Field()
    topics = scrapy.Field()
    media_link = scrapy.Field()
    status = scrapy.Field()
    topics_list = scrapy.Field()
    answerCount = scrapy.Field()
    browse_count = scrapy.Field()
    commentCount = scrapy.Field()
    follow_count = scrapy.Field()
    collapsedAnswerCount = scrapy.Field()
    author_id = scrapy.Field()
    author_url = scrapy.Field()
    isMuted = scrapy.Field()
    isVisible = scrapy.Field()
    isNormal = scrapy.Field()
    isEditable = scrapy.Field()
    reviewInfo = scrapy.Field()
    relatedCards = scrapy.Field()
    adminClosedComment = scrapy.Field()
    hasPublishingDraft = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()
