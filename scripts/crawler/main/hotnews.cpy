from hmac import new
import json
from news import Comment, Event
import re
from time import struct_time
import requests
from bs4 import BeautifulSoup
from htmlparser import HtmlParser

import asyncio
import sys
import website
from db import db


class Media():
    @staticmethod
    def show_in_cmd(list):
        # print(list)
        for news in list:
            print(news)

url_list = []
data_list = {}

async def get_ctx(url):
    HtmlParser(url).run()

async def fetch_data(url):
    await get_ctx(url)

    data_list[url.name] = url.records

    for r in url.records:
        if isinstance(r, Event):
            c = Comment()
            comments = website.init_comments_for_event(r, c)

            for c in comments:

                for url in c.urls:
                    await get_ctx(url)


async def work():
    events = website.init_events()
    task_list = []

    for e in events:
        for url in e.urls:
            url_list.append(url)

    for url in url_list:
        task = loop.create_task(fetch_data(url))
        task_list.append(task)

    await asyncio.wait(task_list)

if __name__ == "__main__":
    # zh_hotnews = ZhiHuNews().get_hot_news()
    # for news in zh_hotnews:
    #     print(news.title, news.link, news.viewcount, news.answercount)
    # ck_hotnews = HotRankNews.get_daily_news("Cankao")
    # Media.show_in_cmd(ck_hotnews)
    # bd_hotnews = HotRankNews.get_daily_news("Baidu")
    # Media.show_in_cmd(bd_hotnews)
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(work())
        
        sys.path.append("../")

        item_list = []
        for url in data_list:
            # Media.show_in_cmd(data_list[url])
            item_list.extend(data_list[url])

        for i in item_list:
            if isinstance(i, Event):
                for c in i.comments:
                    for r in c.refer.records:
                        print(i)
                        print('------------')
                        print(r)
        news = []
        for i in item_list:
            if isinstance(i, Event):    
                for c in i.comments:
                    for r in c.refer.records:
                        t = (i.title, i.link, i.source.name, r.title, r.link, str(i.ner), str(i.kw), i.hot)
                        print(t)
                        db.insert_single_news(t)
                        # news.append(t)
            else:
                t = (i.title, i.link, i.source.name, "", "", str(i.ner), str(i.kw), i.hot)
                print(t)
                db.insert_single_news(t)
                # news.append(t)

        # db.insert_multiple_news(news)
        # t = ('苏炳添晋级百米半1111决赛', '', 'weibo', '苏炳添晋级百米半决赛,最后转头绝了!网友:这是凭实力!_米...', 'http://www.baidu.com/link?url=2lG5UMjUkdfgZxHCDfCDgQguCa1Vx03E_V6nN5R5YMi7Ara17xwYGQYFrNDEdAcX4B9NMd4RUsUkspuo3qDc6q', "['苏炳添']", "['晋级', '百米', '半决赛']", 1)
        # t = ('  #吴亦凡涉嫌强奸被刑拘#', '', 'baidu', '吴亦凡涉嫌强奸罪被警方刑事拘留,他或将承担怎样的法律责...', 'http://www.baidu.com/link?url=vJzIJMuR-rtFlG2IryE4YRn4gSxRmQdH8hNmOKdDdyMcA91Ysl1dvUn5Xsux4-5g1zBLjwlCW5-4Fo4aUP2bKgyOloSpAYeyb4KOst11Uai', "['吴亦凡']", "['涉嫌', '强奸', ' ', '刑拘']", 1)
        # db.insert_single_news(t)
    except:
        raise



