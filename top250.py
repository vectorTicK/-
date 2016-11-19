# -*- coding:utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.request
import os
from bs4 import BeautifulSoup

# 豆瓣TOP250电影类
class TOP250:
    # 初始化方法，定义一些变量
    def __init__(self):

        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}

        self.url = 'https://movie.douban.com/top250?start='
        self.movies = []
        self.current_page = 0

    def getmovie(self, page):
        url = self.url+str(page*25)
        request = urllib.request.Request(url, headers=self.headers)
        response = urlopen(request)
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content)
        items = soup.find(attrs={"class": "grid_view"}).findAll('li')

        for item in items:
            # movie = [电影名，电影链接]
            movie = []
            # 电影名
            title = u''
            titles = item.findAll(attrs={"class": "title"})
            for one in titles:
                title += one.string
            movie.append(title)
            # 电影介绍链接
            link = item.find('a')['href']
            movie.append(link)
            # 电影海报缩略图
            thumb = item.find('a').find('img')['src']
            movie.append(thumb)
            self.movies.append(movie)
        return

        # 创建新目录

    def getmoviedetailinfo(self, movieurl):
        details = [u"导演：", u"主演：", u"简介:"]
        try:
            request = urllib.request.Request(movieurl, headers=self.headers)
            response = urlopen(request)
            content = response.read().decode('utf-8')
            soup = BeautifulSoup(content)
            info = soup.find(id='info').find_all('span')
            # 导演
            details[0] += info[0].a.string
            # 主演
            for item in info[6].find_all('a'):
                details[1] += item.string
                details[1] += " "
            # 简介
            short = soup.find('span', attrs={"property": "v:summary"})
            for string in short.strings:
                details[2] += string.strip()
            return details
        except :
            return details


    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print(u"偷偷新建了名字叫做", path, u'的文件夹')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(u"名为", path, '的文件夹已经创建成功')
            return False

    # 传入图片地址，文件名，保存单张图片
    def save_img(self, image_url, filename):
        u = urlopen(image_url)
        data = u.read()
        f = open(filename, 'wb')
        f.write(data)
        f.close()

    def savetext(self, content, filename):
        f = open(filename, "w+")
        print(u"正在电影信息信息为", filename)
        f.write(content)
        f.close()

top250 = TOP250()
pagenum = 0

while pagenum < 1:
    top250.getmovie(pagenum)
    print(u"正在读取电影。。。。")
    pagenum += 1
print(u"电影读取完毕")

index = 1
for i in top250.movies:
    print(i[0])
    print(i[1])

    # save img
    splitPath = i[2].split('.')
    fTail = splitPath.pop()
    name = str(index) + '.' + i[0].split('/')[0].strip()
    top250.mkdir(name)
    filename = "./" + name + "/" + u"thumb." + fTail
    top250.save_img(i[2], filename)

    movieinfo = top250.getmoviedetailinfo(i[1])
    print(movieinfo[0])
    textname = "./" + name + "/" + name + ".txt"
    textcontent = "\n".join(movieinfo)
    top250.savetext(textcontent, textname)
    print(u"保存%s"%i[0])
    index += 1
