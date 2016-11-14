# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
 
#糗事百科爬虫类
class QSBK:
 
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1

        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = True
    #传入某一页的索引获得页面代码

    def getStorys(self, pageIndex):
		url = 'http://www.qiushibaike.com/8hr/page/' + str(pageIndex)
		request = urllib2.Request(url,headers = self.headers)
		response = urllib2.urlopen(request)

		content = response.read().decode('utf-8')
		soup = BeautifulSoup(content)

		jokes = soup.findAll(attrs={"class":"article block untagged mb15"})
		print u'第%d页'%(self.pageIndex)
		i = 0
		for joke in jokes:
			print u'笑话'+str(i)
			for string in joke.span.strings:
				print string
			print
			i +=1
		print u'第%d页'%(self.pageIndex)
			

    def start(self):
    	print u'"Enter"打印一页笑话，"q"退出'
    	while self.enable:
			input = raw_input()
			if input == "q":
				self.enable = False
				return
			self.getStorys(self.pageIndex)
			self.pageIndex += 1
 
 
spider = QSBK()
spider.start()