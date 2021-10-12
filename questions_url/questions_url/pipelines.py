# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class QuestionsUrlPipeline:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI')
        )

    def open_spider(self, spider):
        # 连接到数据库
        self.client = MongoClient(self.mongo_uri)
        # 连接到指定的数据库
        myDB = self.client['zhihu_Questions']
        # 连接到指定表
        self.myCol = myDB['questions_url']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 存储问题基本信息到MongoDB
        self.myCol.update({'id': item['id']}, {'$set': item}, True)
        print('问题', item['id'], 'url爬取成功！！！')
