# from bs4 import StopParsing
# import utils.nlp.tool as a
# import requests
# from bs4 import BeautifulSoup
import re
import json

from bs4.element import SoupStrainer

# # a.test()

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) \
#             Gecko/20100101 Firefox/34.0",
#         }
# # url = "https://www.baidu.com/s?wd=%E9%99%88%E6%A2%A6%E5%A5%A5%E8%BF%90%E5%A5%B3%E5%8D%95%E5%A4%BA%E9%87%91%20site%3Azhihu.com&rsv_spt=1&rsv_iqid=0x920d6ab300000bfc&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&oq=site%253Azhihu.com&rsv_btype=t&inputT=1221&rsv_t=3e07prXTwXyvEzJqtJqu1%2FigA8dDna%2BMdE%2B6mDmEvof6V1ZazhhLp4yFanoNhemJkD92&rsv_sug3=17&rsv_n=2&rsv_pq=ac406284000066e4&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1747"
# url = "https://www.baidu.com/s?wd=粮食&lm=1"
# c = requests.get(url, headers=headers, verify=False)
# ctx = BeautifulSoup(c.text, 'html.parser')
# div = ctx.find('div', attrs={"id":'content_left'}).find('div', {'class' : 'result c-container new-pmd'});
# print(div.a.attrs["href"])
# # print(ctx)


# import requests

# if __name__ == "__main__":
#     # 定义url的地址
#     url = r'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&'
#     # 定义搜索内容
#     kw = '秦国'
#     param = {
#         'wd': kw
#     }
#     # 伪装请求头
#     head = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
#     # 发起请求
#     response = requests.get(url=url, params=param, headers=head, verify=False)
#     # 获取请求结果
#     result = response.text
#     # 定义储存结果的文件名
#     filename = kw+'.html'
#     # 存储文件
#     with open(filename, 'w', encoding='utf-8') as tem:
#         tem.write(result)
#     print(filename, '保存成功')

# 导入BaiduSpider
# from baiduspider import BaiduSpider
# from pprint import pprint

# # 实例化BaiduSpider
# spider = BaiduSpider()

# # 搜索网页
# # pprint(spider.search_web(query='陈梦奥运女单夺金 site:zhihu.com'))
# ctx = spider.search_web(query='陈梦奥运女单夺金 site:zhihu.com')
# # pattern = r'title\W+(\w+)\W'
# # pattern = r'title'
# # m = re.search(pattern, json.dumps(ctx))
# # print(m[0])
# list = [i for i in ctx["results"] if "title" in i]
# pprint(ctx)
list = [1, 2, 3]
print(eval(str(list)))