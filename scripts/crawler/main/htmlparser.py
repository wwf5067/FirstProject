from bs4 import BeautifulSoup
from website import Url
from news import Record, Event, Comment
import json
from baiduspider import BaiduSpider
import time
import sys
import random

sys.path.append("../")
import utils.nlp.tool as nlp

PATTERNS = ["p_zhihu_hot", "p_wechat_hot", "", "p_bdsearch"]

class HtmlParser():
    def __init__(self, url):
        self.url = url
        self.content = []
        self.spider = BaiduSpider()

    def basic_wrap(self):
        self.content = BeautifulSoup(self.url.get_content(), 'html.parser')

    def match_pattern(self):
        idx = self.url.pattern
        if(idx < len(PATTERNS)):
            m = getattr(self, PATTERNS[idx])
            print(idx)
            m()
        else:
            raise 

    def p_wechat_hot(self):
        tds = self.content.find('tbody').find_all('td', {'class':'al'})
        for td in tds:
            a_tag = td.a
            e = Event()
            e.title = a_tag.get_text()
            e.link = ""
            e.hot = 1
            e.ner, e.kw = nlp.getKW(e.title)
            # e.link = a_tag.attrs["href"]
            # if e.title != "":
            #     c = Comment()
            #     c.title, c.link = self.p_bdsearch(e.title)
            #     e.comment = c
            self.url.add_record(e)

            # print(a_tag.attrs["href"])
            if len(self.url.records) >= 15:
                break

    #for zhihu website
    def p_zhihu_hot(self):
        hot_data = self.content.find('script', id='js-initialData').string
        hot_json = json.loads(hot_data)
        hot_list = hot_json['initialState']['topstory']['hotList']
        for record_ in hot_list:
            c = Comment()
            c.title = str(record_["target"]['titleArea']['text']).replace(" ", "")
            c.link = record_["target"]["link"]["url"]
            c.viewcount = str(record_["target"]["metricsArea"]["text"]).replace(" ", "")
            c.answercount = record_["feedSpecific"]["answerCount"]
            c.hot = 1
            c.ner, c.kw = nlp.getKW(c.title)
            
            self.url.add_record(c)

            if len(self.url.records) >= 10:
                break

    def p_bdsearch(self):
        # div = self.content.find('div', attrs={"id":'content_left'}).find('div', {'class' : 'result c-container new-pmd'});
        # r = Record()
        # r.title = div.a.text
        # r.link = div.a.attrs["href"]
        # self.url.add_record(r)
        # print(r.title)
        # return (div.a.get_text(), div.a.attrs["href"])
        print(self.url.site.name)
        q = '{}'
        if self.url.site.name == "wechat":
            q = q + '' 
        else:
            q = q + 'site:www.zhihu.com'
        
        ctx = self.spider.search_web(query=q.format(self.url.name))
        time.sleep(random.randint(3, 8))
        rst = [i for i in ctx["results"] if "title" in i]
        print(ctx)
        # rst = []
        r = Record()
        r.title = ""
        r.link = ""
        if len(rst) > 0:
            r.title = rst[0]["title"]
            r.link = rst[0]["url"]
        self.url.add_record(r)


    def run(self):
        self.basic_wrap()
        self.match_pattern()