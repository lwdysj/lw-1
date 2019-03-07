#! /usr/bin/python3 env
# -*- coding:utf-8 -*-'

'''
Created on 2018年10月16日

@author: liwei
'''

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError, URLError
from mylog import MyLog
import re, codecs, random

class Item(object):
    name = None
    content = None

class GetData(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/subject/26266893/reviews?start='
        self.log = MyLog()
        self.urls = self.get_urls()
        self.items = self.spider()
        self.pipelines()
        
    def get_urls(self):
        pages = 60
        urls = []
        for i in range(0, pages, 20):
            url = self.url + str(i)
            urls.append(url)
            self.log.info(u'导入URL 成功')
        return urls
    
    def get_response(self, url):
        flag = True
        ua = UserAgent()
        while flag:
            with open('new4proxy.txt', 'r') as fp:
                lines = fp.readlines()
                index = random.randint(1, len(lines))
                proxys = 'https://' + lines[index-1]
            
            fakeHeaders = {'User-Agent':ua.random}
            request = urllib.request.Request(url, headers=fakeHeaders)
                
            proxy = urllib.request.ProxyHandler({'https':proxys})
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)
        
            try:
                response = urllib.request.urlopen(request)
                flag = False
                self.log.info(u'导入URL: 成功')
                return response
            except (HTTPError, URLError):
                flag = True
                self.log.error(u'导入URL: 失败')
        
    def spider(self):
        items = []
        for url in self.urls:
            response = self.get_response(url)
            try:
                item = Item()
                soup = BeautifulSoup(response.read(), 'html.parser')
                item.name = soup.find('a', {'class': 'name'}).text
                item.content = soup.find('div', {'class': 'short-content'}).text
                items.append(item)
                self.log.info(u'获取%s信息: 成功' % item.name)
            except AttributeError:
                self.log.info(u'url None')
        return items
    
    def pipelines(self):
        filename = 'newdata.txt'
        with codecs.open(filename, 'w', 'utf8') as fp:
            for item in self.items:
                fp.write('%s \t %s \n' % (item.name, item.content))
                self.log.info(u'%s保存至%s:成功' % (item.name, filename))

if __name__ == '__main__':
    GM = GetData()
