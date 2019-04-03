# -*- coding: utf-8 -*-

# Scrapy settings for dianping_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dianping_spider'

SPIDER_MODULES = ['dianping_spider.spiders']
NEWSPIDER_MODULE = 'dianping_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dianping_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS ={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'm.dianping.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'm.dianping.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Cookie':'__mta=246904379.1554171817875.1554175923446.1554175963522.18; _lxsdk_cuid=169dbdbed70c8-0fba4e87d5357f8-4c312c7c-1fa400-169dbdbed71c8; _lxsdk=169dbdbed70c8-0fba4e87d5357f8-4c312c7c-1fa400-169dbdbed71c8; _hc.v=8ec2123c-0d74-90f0-e2b1-601e80a4c557.1554171818; cityid=7; default_ab=shop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cmyinfo%3AA%3A1; switchcityflashtoast=1; dp_pwa_v_=1672865b011de2e1f16a640b5af838452230dcb0; dper=a64134eeee20980a4c6a0cbc6487aa71e185960ba2d6947d4af7a5ea0dc1558805e52b45a20985214148403425dfb6dfe5f7038d3edae1ff426245d3da1b0ed8d729ff7ef32c2f4ec983e01d15a0dc81cadde7c969f3c2727ac70251005b6df0; ua=%E5%98%89%E9%91%AB_5900; ctu=30411ce96e17250b0ae66611bf55c0121debd48779b6c687b95cb79fbc623029; _lxsdk_s=169dbfe48da-e56-2b9-215%7C1078351115%7C593; msource=default; chwlsource=default; ll=7fd06e815b796be3df069dec7836c3df; logan_session_token=w63ax1lc96i7hb22xubz; logan_custom_report=',
            'Origin': 'https://m.dianping.com',
            # 'Cookie': 'BAIDUID=77126E8B6D0B7FA20C19EA7A95A65925:FG=1; BIDUPSID=77126E8B6D0B7FA20C19EA7A95A65925; PSTM=1553474892; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; PSINO=6; H_PS_PSSID=1421_21109_28775_28724_28557_28584_28604_28626_28605',
        }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dianping_spider.middlewares.DianpingSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'dianping_spider.middlewares.UAMiddleware': 101,
   # 'dianping_spider.middlewares.ProxyMiddleware': 100,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'dianping_spider.pipelines.DianpingSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


DOWNLOAD_TIMEOUT = 10

MONGO_URI = '127.0.0.1'
MONGO_DATABASE = 'dianping'

REDIS_URL = 'redis://user:@127.0.0.1:6379'

SCHEDULER_PERSIST = True
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
