
class Record():
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    
    @property
    def viewcount(self):
        return self._viewcount

    @viewcount.setter
    def viewcount(self, value):
        self._viewcount = value

    @property
    def ner(self):
        return self._ner

    @ner.setter
    def ner(self, value):
        self._ner = value

    @property
    def kw(self):
        return self._kw

    @kw.setter
    def kw(self, value):
        self._kw = value

    @property
    def hot(self):
        return self._hot

    @hot.setter
    def hot(self, value):
        self._hot = value

    def __str__(self) -> str:
        # return "[{}|{}|{}]".format(self.source,self.title,self.link)
        return "[{}|{}]".format(self.link,self.title)

class Event(Record):
    def __init__(self) -> None:
        super().__init__()
        self._comments = []
        
    def add_comment(self, comment):
        self._comments.append(comment)
        # link = ""
        # u = Url(self.title, link, 'zhihu_search', 3)
        # self._commenturl = u
        # return self._commenturl

    @property
    def comments(self):
        return self._comments
    

    def __str__(self) -> str:
        # return "[{}|{}|{}]".format(self.source,self.title,self.comment)
        return "[{}|{}]".format(self.source,self.title)


class Comment(Record):
    @property
    def refer(self):
        return self._refer

    @refer.setter
    def refer(self, url):
        self._refer = url

    @property
    def answercount(self):
        return self._answercount

    @answercount.setter
    def answercount(self, value):
        self._answercount = value    