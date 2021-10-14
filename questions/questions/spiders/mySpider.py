import scrapy
import datetime
import time
import pymongo
from questions.settings import DATETIME_FORMAT
from questions.settings import MONGO_URI
from questions.items import QuestionsItem
from lxml import etree
import json


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    # allowed_domains = ['www.xxx.com']

    # 从MongoDB获取问题id
    myClient = pymongo.MongoClient(MONGO_URI)
    myDB = myClient['zhihu_Questions']
    myCol = myDB['questions_url']
    question_id_list = myCol.find({}, {'_id': 0, 'id': 1})

    question_url = 'https://www.zhihu.com/question/{question_id}'

    def start_requests(self):
        for question_id in self.question_id_list:
            yield scrapy.Request(self.question_url.format(question_id=question_id['id']), headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'},
                                 callback=self.parse_question)
            time.sleep(1)

    def parse_question(self, response):
        json_text_content = response.xpath("//script[@id='js-initialData']/text()").get()
        time.sleep(1)
        json_content = json.loads(json_text_content)
        question_id = response.url.split('/')[-1]
        print('#########################')
        print('正在爬取问题', question_id)
        question_item = QuestionsItem()
        question = json_content['initialState']['entities']['questions'][str(question_id)]
        question_item['id'] = question['id']
        question_item['url'] = question['url']
        question_item['type'] = question['questionType']
        question_item['title'] = question['title']
        question_item['description'] = question['excerpt']
        question_item['detail'] = question['detail']
        question_item['editableDetail'] = question['editableDetail']
        question_item['status'] = question['status']
        question_item['topics_list'] = question['topics']
        question_item['topics'] = []
        for topic in question['topics']:
            question_item['topics'].append(topic['name'])
        if etree.HTML(question['detail']) is not None:
            question_item['media_link'] = ';'.join(etree.HTML(question['detail']).xpath("//img/@src"))
        else:
            question_item['media_link'] = ''
        question_item['answerCount'] = int(question['answerCount'])
        question_item['browse_count'] = int(question['visitCount'])
        question_item['commentCount'] = int(question['commentCount'])
        question_item['follow_count'] = int(question['followerCount'])
        question_item['collapsedAnswerCount'] = int(question['collapsedAnswerCount'])
        question_item['author_id'] = question['author']['id']
        question_item['author_url'] = question['author']['url']
        question_item['isMuted'] = question['isMuted']
        question_item['isVisible'] = question['isVisible']
        question_item['isNormal'] = question['isNormal']
        question_item['isEditable'] = question['isEditable']
        question_item['adminClosedComment'] = question['adminClosedComment']
        question_item['hasPublishingDraft'] = question['hasPublishingDraft']
        question_item['reviewInfo'] = question['reviewInfo']
        question_item['relatedCards'] = question['relatedCards']
        question_item["create_time"] = datetime.datetime.fromtimestamp(question["created"]).strftime(
            DATETIME_FORMAT)
        question_item["update_time"] = datetime.datetime.fromtimestamp(question["updatedTime"]).strftime(
            DATETIME_FORMAT)
        question_item["crawl_time"] = datetime.datetime.now().strftime(DATETIME_FORMAT)

        yield question_item
