# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup


# 糗事百科爬虫类
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1

        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放程序是否继续运行的变量
        self.enable = True

    def get_jokes(self, page_index):
        url = 'http://www.qiushibaike.com/8hr/page/' + str(page_index)
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content)
        jokes = soup.findAll(attrs={"class": "article block untagged mb15"})
        print u'第%d页' % page_index
        i = 0
        for joke in jokes:
            print u'笑话' + str(i)
            for string in joke.span.strings:
                print string
            print
            i += 1
        print u'第%d页' % page_index

    def start(self):
        print u'"Enter"打印一页笑话，"q"退出'
        while self.enable:
            input_cmd = raw_input()
            if input_cmd == "q":
                self.enable = False
                return
            self.get_jokes(self.pageIndex)
            self.pageIndex += 1


spider = QSBK()
spider.start()
