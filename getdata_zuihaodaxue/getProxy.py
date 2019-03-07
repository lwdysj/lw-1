#! /usr/bin/python3 env
# -*- coding:utf-8 -*-

'''
Created on 2018年10月16日

@author: liwei
'''

import urllib.request
from bs4 import BeautifulSoup

#获取免费匿名代理
class Item(object):
    ip = None
    
class GetProxy(object):
    def __init__(self):
        self.url = 'http://www.66ip.cn/'
        self.urls = self.get_urls()
        self.items = self.spider()
        self.pipelines()
        print(u'存入结束')
        
    def get_urls(self):
        urls = []
        pages = 200
        for i in range(1, pages + 1):
            url = self.url + str(i) + '.html'
            urls.append(url)
            print(u'正在读取URL')
        return urls
    
    def spider(self):
        items = []
        for url in self.urls:
            response = urllib.request.urlopen(url)
            soup = BeautifulSoup(response.read(), 'lxml')
            tags = soup.find('table', {"border":"2px"}).find_all('tr')
            for tag in tags[1:]:
                item = Item()
                item.ip = tag.find_all('td')[0].get_text() + ':' + tag.find_all('td')[1].get_text()
                items.append(item)
                print(u'正在获取数据')
        return items
    
    def pipelines(self):
        filename = 'proxy.txt'
        with open(filename, 'a') as fp:
            for item in self.items:
                fp.write(item.ip + '\n')
                print(u'正在存入')

if __name__ == '__main__':
    GP = GetProxy()            
