# -*- coding: utf-8 -*-
import json
import re

from scrapy import Spider, Request
from dianping_spider.items import Item


class DpSpider(Spider):
    name = 'dp'
    allowed_domains = ['dianping.com']
    # 获取购物品类的url
    shop_type_url = 'http://www.dianping.com/shenzhen/ch20/g119'
    # 商品详情页的url，拼接商品的uuid
    shop_detail_url = 'https://m.dianping.com/shop/{uuid}'
    # 商圈的api接口
    mall_api = 'https://mapi.dianping.com/shopping/mall/channel/nearbylist?cityid=7&page={page}&pagesize=100'
    # # 商圈的url, 拼接商圈的id
    # mail_url = 'https://m.dianping.com/shopping/node/mall/shoplist.html?mallid={}'
    # 特定商圈内购物品类的接口
    mail_type_url = 'https://mapi.dianping.com/shopping/mall/shops?mallid={mail_id}&latitude=0&longitude=0&utm_source' \
                    '=&query=2-{type_id}&page=1&pagesize=20 '
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Host': 'mapi.dianping.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Cookie': 'cityid=7; _hc.v=fb07d859-8af5-e65c-df08-02e837464e13.1554195931; '
                      'default_ab=shop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1; '
                      '_lxsdk_cuid=169dd4be240c8-09f693a04c2ba68-4c312c7c-1fa400-169dd4be241c8; '
                      '_lxsdk=169dd4be240c8-09f693a04c2ba68-4c312c7c-1fa400-169dd4be241c8; '
                      'pvhistory=6L+U5ZuePjo8L2Vycm9yL2Vycm9yX3BhZ2U+OjwxNTU0MjExMDAxNzk3XV9b; m_flash2=1; '
                      '_lx_utm=utm_source%3Dshoppinghome; s_ViewType=10; cy=7; cye=shenzhen; switchcityflashtoast=1; '
                      'source=m_browser_test_33; _lxsdk_s=169e120656b-461-748-1d3%7C0%7C3; msource=default '

    }
    shop_types = ['33943', '120', '119', '121', '187', '2714', '33760', '235', '34124', '34149', '33944', '123', '128', '125', '124', '33906', '34204', '2776', '33858', '6716', '34269', '34208', '32698', '130', '127', '126', '129', '26101', '33905', '34114', '32720', '34207', '32739', '131']

    max_page = 7

    def start_requests(self):
        """请求获取购物品类的url,商圈的api接口"""
        # yield Request(url=self.shop_type_url, callback=self.parse_shop_type, headers=self.headers)
        # 请求商圈api接口
        for page in range(1, self.max_page):
            # self.headers['Host'] = 'mapi.dianping.com'
            yield Request(url=self.mall_api.format(page=page), callback=self.parse_mail_id, headers=self.headers)

    def parse_shop_type(self, response):
        # 获取购物类型
        self.shop_types = response.xpath('//div[@id="classfy"]//a/@data-cat-id').getall()
        print(self.shop_types)

    def parse_mail_id(self, response):
        """解析商圈id,名字"""
        mail_json = json.loads(response.text)
        # 循环获取每个商圈的id,名字
        for mail_info in mail_json['msg']['mallList']:
            mail_id = mail_info['id']
            mail_regionName = mail_info['regionName']
            # 每个商圈,根据购物类型api循环获取店铺
            for type_id in self.shop_types:
                self.headers['Host'] = 'mapi.dianping.com'
                yield Request(url=self.mail_type_url.format(mail_id=mail_id, type_id=type_id),
                              callback=self.parse_shop_id, headers=self.headers,
                              meta={'mail_id': mail_id, 'mail_regionName': mail_regionName})

    def parse_shop_id(self, response):
        """解析店铺id,店铺名字,店铺url"""
        shop_json = json.loads(response.text)
        mail_id = response.meta['mail_id']
        mail_regionName = response.meta['mail_regionName']
        # 判断该商圈是否有对应类型的返回,有就解析
        if shop_json['msg'] is not None:
            for shop_info in shop_json['msg']['shops']:
                shop_id = shop_info['shopId']
                shop_name = shop_info['shopName']
                shop_url = self.shop_detail_url.format(uuid=shop_id)
                self.headers['Host'] = 'm.dianping.com'
                # 根据店铺url进入详情页
                yield Request(url=shop_url, callback=self.parse_shop_detail,
                              meta={'mail_id': mail_id, 'mail_regionName': mail_regionName,
                                    'shop_id': shop_id, 'shop_name': shop_name})

    def parse_shop_detail(self, response):
        """获取店铺地址"""
        meta = response.meta
        item = Item()
        item['shop_address'] = response.xpath('//textarea[@id="shop-detail"]/text()').re_first(r'"address":"(.*?)"')
        item['shop_url'] = response.url
        item['mail_id'] = meta['mail_id']
        item['mail_regionName'] = meta['mail_regionName']
        item['shop_id'] = meta['shop_id']
        item['shop_name'] = meta['shop_name']
        yield item








