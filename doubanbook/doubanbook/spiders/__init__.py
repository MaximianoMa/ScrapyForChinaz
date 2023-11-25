import scrapy
from doubanbook.items import CaoItem

class CaoSpider(scrapy.Spider):
    name = "cao"
    allowed_domains = ['chinaz.com']
    start_urls = [
        'https://top.chinaz.com/hangye/index_yule.html',
        'https://top.chinaz.com/hangye/index_shopping',
        'https://top.chinaz.com/hangye/index_gov',
        'https://top.chinaz.com/hangye/index_zonghe',
        'https://top.chinaz.com/hangye/index_jiaoyu',
        'https://top.chinaz.com/hangye/index_qiye',
        'https://top.chinaz.com/hangye/index_shenghuo',
        'https://top.chinaz.com/hangye/index_wangluo',
        'https://top.chinaz.com/hangye/index_tiyu',
        'https://top.chinaz.com/hangye/index_yiliao',
        'https://top.chinaz.com/hangye/index_jiaotonglvyou',
        'https://top.chinaz.com/hangye/index_news'
    ]

    def __init__(self, *args, **kwargs):
        super(CaoSpider, self).__init__(*args, **kwargs)
        self.page_counter = 0
        self.start_url_index = 0

    def start_requests(self):
        yield scrapy.Request(self.start_urls[self.start_url_index], self.parse)

    def parse(self, response):
        # Process the current page
        yield from self.parse_page(response)

        # Check if 10 pages have been crawled
        if self.page_counter >= 10:
            # Reset the counter
            self.page_counter = 0
            # Move to the next start URL
            self.start_url_index += 1
            if self.start_url_index < len(self.start_urls):
                next_start_url = self.start_urls[self.start_url_index]
                yield scrapy.Request(next_start_url, self.parse)
            return  # Stop processing the current start URL

        # Pagination logic as before
        # ...

    def parse_page(self, response):
        self.page_counter += 1
        # Your existing page parsing logic
        # ...

    # Other methods (parse_details, etc.) remain unchanged
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
