# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup


# 百度贴吧爬虫类
class BDTB:

    # 初始化
    def __init__(self, base_url, see_lz):
        self.base_url = base_url
        self.see_lz = '?see_lz=' + str(see_lz)
        self.first_page = self.get_page(1)
        self.soup = BeautifulSoup(self.first_page)

    # 传入页码，获取该页帖子的代码
    def get_page(self, page_num):
        try:
            url = self.base_url + self.see_lz + '&pn=' + str(page_num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,错误原因", e.reason
                return None

    def get_title(self):
        # 获取帖子标题
        result = self.soup.find(attrs={'class': "core_title_txt pull-left text-overflow  "})
        if result:
            # print result.group(1)  #测试输出
            return result.string
        else:
            return None

    def get_page_count(self):
        # 获取帖子页数
        count = self.soup.find(attrs={'class': "l_reply_num"}).findAll(attrs={'class': "red"})[1]
        if count:
            return count.string
        else:
            return None

    def get_content(self, page_num):
        page = self.get_page(page_num)
        soup = BeautifulSoup(page)
        content = soup.findAll(attrs={'class': "d_post_content j_d_post_content "})
        floors = []
        if content:
            for floor in content:
                one = u''
                for string in floor.strings:
                    one += string.strip()
                    one += '\n'
                floors.append(one)
            return floors
        else:
            return None

    def write_data(self,contents):
        # 向文件写入每一楼的信息
        title = bdtb.get_title()
        filew = open(title + ".txt", "w+")
        for item in contents:
            filew.write(item.encode('utf-8'))

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)

title = bdtb.get_title()
print u'标题:%s' % title
#
page_count = bdtb.get_page_count()
print u'回帖页数:%s' % page_count

content = bdtb.get_content(2)
for one in content:
    print one
bdtb.write_data(content)



