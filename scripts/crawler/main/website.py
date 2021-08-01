import re
import requests
from urllib.parse import urlparse

SITES = {
    "Events": {
        "zhihu": {
            "uscale":25, 
            "links":[
                ["zhot", "https://www.zhihu.com/billboard", 25, 0]
            ]
        },
        "wechat": {
            "uscale":30,
            "links":[
                ["whot", "https://tophub.today/n/WnBe01o371", 20, 1]
            ]
        },
        "weibo": {
            "uscale":28,
            "links":[
                ["wbhot", "https://tophub.today/n/KqndgxeLl9", 22, 1]
            ]
        },
        "baidu": {
            "uscale":27,
            "links":[
                ["bdhot", "https://tophub.today/n/Jb0vmloB1G", 21, 1]
            ]
        }
    },
    "Comments": {
        "bdsearch": {
            "uscale":27,
            "links":[
                ["zhihu","https://www.baidu.com/s?wd={}%20site%3Azhihu.com&"\
                "rsv_spt=1&rsv_iqid=0x920d6ab300000bfc&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&"\
                "oq=site%253Azhihu.com&rsv_btype=t&inputT=1221&rsv_t=3e07prXTwXyvEzJqtJqu1%2FigA8dDna%2BMdE%2B6mDmEvof6V1ZazhhLp4yFanoNhemJkD92&"\
                "rsv_sug3=17&rsv_n=2&rsv_pq=ac406284000066e4&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1747", 21, 3]
            ]
        }
    }
}
# SITES = {
#     "Events": {
#         # "zhihu": {
#         #     "uscale":25, 
#         #     "links":[
#         #         ["zhot", "https://www.zhihu.com/billboard", 25, 0]
#         #     ]
#         # },
#         "wechat": {
#             "uscale":30,
#             "links":[
#                 ["whot", "https://tophub.today/n/WnBe01o371", 20, 1]
#             ]
#         },
#         # "weibo": {
#         #     "uscale":28,
#         #     "links":[
#         #         ["wbhot", "https://tophub.today/n/KqndgxeLl9", 22, 1]
#         #     ]
#         # },
#         "baidu": {
#             "uscale":27,
#             "links":[
#                 ["bdhot", "https://tophub.today/n/Jb0vmloB1G", 21, 1]
#             ]
#         }
#     },
#     "Comments": {
#         "bdsearch": {
#             "uscale":27,
#             "links":[
#                 ["zhihu","https://www.baidu.com/s?wd={}%20site%3Azhihu.com&"\
#                 "rsv_spt=1&rsv_iqid=0x920d6ab300000bfc&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&"\
#                 "oq=site%253Azhihu.com&rsv_btype=t&inputT=1221&rsv_t=3e07prXTwXyvEzJqtJqu1%2FigA8dDna%2BMdE%2B6mDmEvof6V1ZazhhLp4yFanoNhemJkD92&"\
#                 "rsv_sug3=17&rsv_n=2&rsv_pq=ac406284000066e4&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1747", 21, 3]
#             ]
#         }
#     }
# }

class Site():
    def __init__(self, name):
        self._name = name
        self._userscale = 0
        self._urls = []

    @property
    def name(self):
        return self._name

    @property
    def userscale(self):
        return self._userscale

    @userscale.setter
    def userscale(self, m):
        self._userscale = 0 | (1 << m)

    @property
    def urls(self):
        return self._urls;

    def add_url_from(self, name, link, m, p):
        url = Url(name, link, self, p)
        url.authority = m
        self._urls.append(url)
        return url

    def __str__(self) -> str:
        return self.name + ":" + str(bin(self.userscale))


class Url():
    def __init__(self, name, link, site, pattern) -> None:
        self.name = name
        self.link = link
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) \
            Gecko/20100101 Firefox/34.0",
        }
        self._authority = 0
        self._site = site
        self._pattern = pattern
        self._records = []
    
    def get_content(self):
        rsp = requests.get(self.link, headers = self.headers, verify = False)
        # print(rsp.text)
        return rsp.text

    @property
    def site(self):
        return self._site

    @property
    def pattern(self):
        return self._pattern
        
    @property
    def authority(self):
        return self._authority

    @authority.setter
    def authority(self, m):
        self._authority = 0 | (1 << m)

    @property
    def records(self):
        return self._records

    def add_record(self, value):
        # record = Record()
        # record.source = self.site
        # record.title = title
        # if href.startswith("https://"):
        #     record.link = href
        # else:
            # record.link = self.link[:self.link.rindex("/")] + href
            # record.link = ""
        value.source = self.site
        self._records.append(value)
        
    def __str__(self) -> str:
        return self.link + ',' + str(bin(self.authority)) +'\n' + str(self.site)
        # return "|".join(self.records)

def init_events():
    sites = []
    for k,v in SITES["Events"].items():
        site = Site(k)
        site.userscale = v["uscale"]


        for v_ in v["links"]:
            url = site.add_url_from(v_[0], v_[1], v_[2], v_[3])
            # print(site)
            sites.append(site)
    return sites

def init_comments_for_event(e, c):
    sites = []
    for v in SITES["Comments"].values():
        site = Site(e.source)
        site.userscale = v["uscale"]

        for v_ in v["links"]:
            url = site.add_url_from(e.title, str(v_[1]).format(e.title), v_[2], v_[3])
            sites.append(site)
            c.refer = url
            e.add_comment(c)

            
    return sites

# init_sites()
