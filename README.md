# zhihu_questions_spider_v3
从知乎推荐页入手，获取问题url，再爬取问题信息及回答（独立进行），使用代理ip，存储到MongoDB

文件介绍：
- questions_url：从推荐页获取问题url
- question：访问每一个问题url，获取问题详细信息
- answers：获取问题对应的回答信息

使用步骤：
- 启动MongoDB服务
- 将ip加入代理ip白名单（极光代理）：若无代理ip需要，可在settings文件中关闭（注释掉）downloadmiddleware
- 运行main函数
