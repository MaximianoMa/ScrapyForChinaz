import scrapy
import re
from doubanbook.items import CaoItem

class CaoSpider(scrapy.Spider):
    name = "cao"
    allowed_domains = ['chinaz.com']
    start_urls = [
        'https://top.chinaz.com/hangye/index_yiliao.html',
        'https://top.chinaz.com/hangye/index_jiaotonglvyou.html',
        'https://top.chinaz.com/hangye/index_shopping.html',
        'https://top.chinaz.com/hangye/index_yule.html',
        'https://top.chinaz.com/hangye/index_gov.html',
        'https://top.chinaz.com/hangye/index_zonghe.html',
        'https://top.chinaz.com/hangye/index_jiaoyu.html',
        'https://top.chinaz.com/hangye/index_qiye.html',
        'https://top.chinaz.com/hangye/index_shenghuo.html',
        'https://top.chinaz.com/hangye/index_wangluo.html',
        'https://top.chinaz.com/hangye/index_tiyu.html',
        'https://top.chinaz.com/hangye/index_news.html'
    ]

    l = {'https://top.chinaz.com/hangye/index_yule.html': '休闲娱乐',
         'https://top.chinaz.com/hangye/index_shopping.html': '购物网站',
         'https://top.chinaz.com/hangye/index_gov.html': '政府组织',
         'https://top.chinaz.com/hangye/index_zonghe.html': '综合其他',
         'https://top.chinaz.com/hangye/index_jiaoyu.html': '教育文化',
         'https://top.chinaz.com/hangye/index_qiye.html': '行业企业',
         'https://top.chinaz.com/hangye/index_shenghuo.html': '生活服务',
         'https://top.chinaz.com/hangye/index_wangluo.html': '网络科技',
         'https://top.chinaz.com/hangye/index_tiyu.html': '体育健身',
         'https://top.chinaz.com/hangye/index_yiliao.html': '医疗健康',
         'https://top.chinaz.com/hangye/index_jiaotonglvyou.html': '交通旅游',
         'https://top.chinaz.com/hangye/index_news.html': '新闻媒体'}





    def __init__(self, *args, **kwargs):
        super(CaoSpider, self).__init__(*args, **kwargs)
        self.start_url_index = 0

    def parse(self, response):
        # Process the current page
        yield from self.parse_page(response)

        # Find the 'Next' page link and check if it is the same as the first pagination link
        next_page = response.xpath('//div[@class="ListPageWrap"]/a[contains(text(), ">")]/@href').extract_first()
        first_pagination_link = response.xpath('//div[@class="ListPageWrap"]/a[@class]/@href').extract_first()

        if next_page != first_pagination_link:
            # Not the last page, continue scraping
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            # Last page, move to the next start URL
            self.start_url_index += 1
            if self.start_url_index < len(self.start_urls):
                next_start_url = self.start_urls[self.start_url_index]
                yield scrapy.Request(next_start_url, callback=self.parse)
            else:
                return

    def parse_page(self, response):
        for item in response.xpath('//div[@class="CentTxt"]'):
            cao = CaoItem()
            cao['url'] = item.xpath('.//span[@class="col-gray"]/text()').extract()[0]
            response_url = response.url
            url_key = re.sub(r'_[0-9]+', '', response_url)
            cao['industry'] = self.l[url_key]
            cao['title'] = item.xpath('.//h3[@class="rightTxtHead"]/a/@title').extract_first()
            if cao['title']:
                link = item.xpath('.//h3[@class="rightTxtHead"]/a/@href').extract_first()
                if link:
                    link = response.urljoin(link)
                    request = scrapy.Request(link, callback=self.parse_details)
                    request.meta['cao'] = cao
                    yield request


    def parse_details(self, response):
        cao = response.meta['cao']
        cao['description'] = response.xpath('.//p[@class="webIntro"]/text()').extract_first()
        cao['keywords'] = set()
        for item in response.xpath('//span[@class="Lnone"]'):
            text = item.xpath('.//text()').extract()[0]
            cao['keywords'].add(text)
        cao['keywords'].discard("百度关键词")
        cao['keywords'].discard("360关键词")
        # cao['keywords'] = response.xpath('').extract_first()
        yield cao
