import re
page_counts = {
    'https://top.chinaz.com/hangye/index_yule.html': 277, 'https://top.chinaz.com/hangye/index_shopping': 89,
    'https://top.chinaz.com/hangye/index_gov': 106,
    'https://top.chinaz.com/hangye/index_zonghe': 282, 'https://top.chinaz.com/hangye/index_jiaoyu': 229,
    'https://top.chinaz.com/hangye/index_qiye': 261,
    'https://top.chinaz.com/hangye/index_shenghuo': 321, 'https://top.chinaz.com/hangye/index_wangluo': 141,
    'https://top.chinaz.com/hangye/index_tiyu': 27,
    'https://top.chinaz.com/hangye/index_yiliao': 53, 'https://top.chinaz.com/hangye/index_jiaotonglvyou': 59,
    'https://top.chinaz.com/hangye/index_news': 66
    # ... other URL page counts ...
}
start_urls = [
        'https://top.chinaz.com/hangye/index_yiliao.html',
        'https://top.chinaz.com/hangye/index_shopping',
        'https://top.chinaz.com/hangye/index_yule.html',
        'https://top.chinaz.com/hangye/index_gov',
        'https://top.chinaz.com/hangye/index_zonghe',
        'https://top.chinaz.com/hangye/index_jiaoyu',
        'https://top.chinaz.com/hangye/index_qiye',
        'https://top.chinaz.com/hangye/index_shenghuo',
        'https://top.chinaz.com/hangye/index_wangluo',
        'https://top.chinaz.com/hangye/index_tiyu',
        'https://top.chinaz.com/hangye/index_jiaotonglvyou',
        'https://top.chinaz.com/hangye/index_news'
        # ... 其他 start_urls ...
    ]

print(start_urls[1])

l = {'https://top.chinaz.com/hangye/index_yule': '休闲娱乐',
     'https://top.chinaz.com/hangye/index_shopping': '购物网站',
     'https://top.chinaz.com/hangye/index_gov': '政府组织',
     'https://top.chinaz.com/hangye/index_zonghe': '综合其他',
     'https://top.chinaz.com/hangye/index_jiaoyu': '教育文化',
     'https://top.chinaz.com/hangye/index_qiye': '行业企业',
     'https://top.chinaz.com/hangye/index_shenghuo': '生活服务',
     'https://top.chinaz.com/hangye/index_wangluo': '网络科技',
     'https://top.chinaz.com/hangye/index_tiyu': '体育健身',
     'https://top.chinaz.com/hangye/index_yiliao': '医疗健康',
     'https://top.chinaz.com/hangye/index_jiaotonglvyou': '交通旅游',
     'https://top.chinaz.com/hangye/index_news.html': '新闻媒体'}
response_url = 'https://top.chinaz.com/hangye/index_news_111.html'
url_key = re.sub(r'_[0-9]+', '', response_url)
print(url_key)
print(l[url_key])