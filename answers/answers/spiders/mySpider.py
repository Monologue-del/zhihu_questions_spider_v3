import scrapy
import datetime
import time
import pymongo
from answers.settings import MONGO_URI
from answers.settings import DATETIME_FORMAT
from answers.items import AnswersItem
import json


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    # allowed_domains = ['www.xxx.com']

    # 从MongoDB获取问题id
    myClient = pymongo.MongoClient(MONGO_URI)
    myDB = myClient['zhihu_Questions']
    myCol = myDB['questions_url']
    question_id_list = myCol.find({}, {'_id': 0, 'id': 1})

    answer_url = 'http://www.zhihu.com/api/v4/questions/{question_id}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=10&sort_by=default&platform=desktop'

    def start_requests(self):
        for question_id in self.question_id_list:
            yield scrapy.Request(self.answer_url.format(question_id=question_id['id']), headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'},
                                 callback=self.parse_answer)
            time.sleep(1)

    def parse_answer(self, response):
        """
        解析答案页面，提取答案信息
        :param response:
        :return:
        """
        # 处理question的answer
        ans_json = json.loads(response.text)
        is_end = ans_json['paging']['is_end']
        next_url = ans_json['paging']['next']

        # 判断问题是否有回答
        if len(ans_json["data"]) == 0:
            pass
        # 提取answer的具体字段
        else:
            for answer in ans_json['data']:
                answer_item = AnswersItem()
                answer_item["answer_id"] = answer["id"]
                print('#########################')
                print('正在爬取答案', answer["id"])
                answer_item["answer_url"] = answer["url"]
                answer_item["question_id"] = answer["question"]["id"]
                answer_item["question_title"] = answer["question"]["title"]
                answer_item["author_id"] = answer["author"]["id"] if "id" in answer["author"] else None
                answer_item["author_name"] = answer["author"]["name"] if "name" in answer["author"] else None
                answer_item["content"] = answer["content"] if "content" in answer else None
                answer_item["praise_num"] = answer["voteup_count"]
                answer_item["comments_num"] = answer["comment_count"]
                answer_item["create_time"] = datetime.datetime.fromtimestamp(answer["created_time"]).strftime(
                    DATETIME_FORMAT)
                answer_item["update_time"] = datetime.datetime.fromtimestamp(answer["updated_time"]).strftime(
                    DATETIME_FORMAT)
                answer_item["crawl_time"] = datetime.datetime.now().strftime(DATETIME_FORMAT)

                yield answer_item

            if not is_end:
                yield scrapy.Request(next_url, callback=self.parse_answer)
                time.sleep(3)
