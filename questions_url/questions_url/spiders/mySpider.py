import json

import scrapy
import time
import json
import datetime
from questions_url.items import QuestionsUrlItem
from questions_url.settings import DATETIME_FORMAT


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=bc86575b6393e3ab19c3223335becf89&desktop=true&limit=7&action=down&after_id=0']

    # 爬取页数计数
    page_count = 1

    def parse(self, response):
        """
        提取推荐页中的所有问题url
        :param response:
        :return:
        """
        print("########################")
        print("正在爬取第%d页" % self.page_count)
        rec_web = json.loads(response.text)

        for item in rec_web['data']:
            # 有时候会出现广告，产生异常
            try:
                item_type = item['target']['type']
                # 如果遇到视频，跳过
                if str(item_type) == "answer":
                    question_data = item['target']['question']
                    question_item = self.parse_question_info(data=question_data)
                    yield question_item
                else:
                    continue
            except Exception:
                continue

        is_end_page = rec_web['paging']['is_end']
        if not is_end_page:
            next_page_url = rec_web['paging']['next']
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        print("第%d页爬取结束" % self.page_count)
        print("-------------------------")
        self.page_count += 1
        time.sleep(3)

    def parse_question_info(self, data):
        """
        简单解析问题信息
        :param data:
        :return:
        """
        question_info = QuestionsUrlItem()
        question_info['id'] = data['id']
        question_info['type'] = data['question_type']
        question_info['url'] = data['url']
        question_info['title'] = data['title']
        question_info["question_createdTime"] = datetime.datetime.fromtimestamp(data["created"]).strftime(
            DATETIME_FORMAT)
        question_info['answer_count'] = data['answer_count']
        question_info['follower_count'] = data['follower_count']
        question_info['comment_count'] = data['comment_count']
        question_info['author_id'] = data['author']['id']
        question_info['author_type'] = data['author']['type']
        question_info['author_url'] = data['author']['url']
        question_info['author_name'] = data['author']['name']
        question_info['author_is_org'] = data['author']['is_org']
        return question_info
