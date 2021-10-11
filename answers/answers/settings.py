# Scrapy settings for answers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'answers'

SPIDER_MODULES = ['answers.spiders']
NEWSPIDER_MODULE = 'answers.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'cookie': '_zap=1b3bfa76-6c11-4b25-a116-4f326c609e05; _xsrf=9NRPNjgstDehs6eUMc8EjE6mP54tSHTd; d_c0="AGCfJxDDfBOPTkoYmDP6bqThvcDJPJvR9ng=|1627570148"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1627570148; __snaker__id=7m6gHKu7YcZbB2NR; _9755xjdesxxd_=32; ISSW=1; YD00517437729195%3AWM_TID=oDn67gG%2Fx39AEQBBEBMv2fsiIERwROLX; tshl=; r_cap_id="ZGIyZGIwMDdhODczNDBhMzhkOTI5ZTdkZjBmNGQ0OWM=|1633507145|98e2c2105c04a6e3118eea9a56baf0e981cb77ae"; cap_id="NTc1YzNhZTYxMWY3NDIyNThiZWMyNTdjZDY1MjEwZmE=|1633507145|6a529d4a76359f50aa3eb8233bcd13057e34faea"; l_cap_id="YmJiZDFiNTY3M2FjNDNkNGJkMTE1YTEzYTgxY2E4NTA=|1633507145|c881adb15d94545e0582eb424c5b01dbdf84d5b1"; q_c1=ea154a8caea649be9d9f4f7219b63a9d|1633507753000|1627616739000; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed3f07e88b69db8d77ba8b88ea2c45a878a9ebaf13495babdd7b34df8b2baa9c22af0fea7c3b92aad90b6d9c567aca7fdaadb4aab9fc0d1f625b18faed4f95289adf98ee44aa2ea8cadc7539a918f96d97aa2eabcaeb56aa6b800a9c95cf693aa92b3678dbe8a97e55fbb97a4a7b253928aa5b3c268bca6a5d6b35db4f0e1aff2648ba98e8ae43994acbaa2bc66869289d1b734a8b6e5baee458bb383d8eb61b1b2fd8fe93a868882b9c837e2a3; YD00517437729195%3AWM_NI=oPz8Fmhy3IXBiAp0w%2FsQb3zZKs7maBb6DLDYZOAuZrb6tM6bfh0HJP6Mfq0mObFvfUyIlF3YRVkRClxzk50Wp0%2FNshIwBia3PtvA9nFNG048dj%2BYoOImM7hksn3nj2FXNXE%3D; gdxidpyhxdE=MpmgBU5YxuYtgnYvusf4x2nRKJVMho9s4ny0nPOMV%5C4BqHBOi%2B9984TBTnwj%2B4NJmMPpp3famyDc8HzbcxrPmzbK7%2BnBBm1DuO4sWLXAvirPyK6bVTLZyyd4tqr0%2B8VK4Td6OS2eGSgD%2Fp2qNCIsdb%5Cvqb%2BaqDvamAN5oX0AirUxDOow%3A1633682635875; captcha_session_v2="2|1:0|10:1633681738|18:captcha_session_v2|88:bnlRYllzcENpZ1Rmam9lS1NVWGExbm5iUkMvb0xEajMrQ3huNmxReXNmblI3ZWxncEIvM0h0TkZKT0VnS1QxOA==|56dbc68784fee981c39a405eafce4051fe73ce82ec3096127e369ebdf3895343"; captcha_ticket_v2="2|1:0|10:1633681742|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfTXJBUl9TakRkUjlBTjlCNmQ1ajVxWDZlTmtEZ1lTWWhQMnp1bWM4dWdDdU5nQ0JDdzRtckhEMV9fY1BNWm5oZ3dTVk5qRUFVV201UUsyZWdWaGJwLXgtU2tOT24uTFNXMFp0SEFYTTFLV3RRQ25MRlE2T3VqT0FyQ0tvU3dQRnN2MlB5SHlNOVl1THBUeW91X1ZHdi01Lml0QUhBVm1ZVlAxUDBJVzhWdHFmek9OZVVvS3BwTHg3YjlwRFB1Rmx1NnRfc3I2WUx1UmtsSGNqRi1LLlVyZnpTcXltTzRTeHVTZFd0Qlp0ejdnam04YUNqODdQcVQ0bDBCcG1nOEJTNDAuNHlBX0xzSWpiU1lpaW8ydkRrWUtOenVudlBHclFpeTFmMmNadjR5b3BFVnlVRDJDbXU4ekJ0eFQ2WS45OUZ5NjZ5dmk1NDlrSEVGZU1vcjA0OVIwLnc3dlVsZ09ldi1DOWZDX1ZpUFh2UEJYZHdqZFFMN043VmtKX2pndXVjZWxvVE9TbVd5SjVpNVJPbi14Y0tNTmtoZnFSaUcyRHVzclZoQ0huOXB0TGpub3dkMWRObG1nTTAxS2kxa0FMWmZpRi1sSi5acFdvQzhsejFmRTR1UWsudldPMFFpQzFBVW9JVEpEZGVzaGZRY2gwdEZoZkJtX2NZMC5hMyJ9|ca0885f3202dec4040fb7756e9a4cebb32311ba9b3d0ec14879251b976618741"; z_c0="2|1:0|10:1633681743|4:z_c0|92:Mi4xWjd5SkRBQUFBQUFBWUo4bkVNTjhFeVlBQUFCZ0FsVk5UMDlOWWdBcHlmRWVGS0pfbTZCQXdEU0tmcVE5M3lJVEZ3|d1cb1e27e7c3b90117e7b745c5108df88cbdced228db3cb0be99ee1bdd66827d"; tst=r; SESSIONID=YeKm3Sd3bHGM4YG5zRbHwO5Ib7wKpPl891snqOqKelj; KLBRSID=3d7feb8a094c905a519e532f6843365f|1633691106|1633681736'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'answers.middlewares.AnswersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'answers.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'answers.pipelines.AnswersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 设置日期格式
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# MongoDB配置
MONGO_URI = 'localhost:27017'
