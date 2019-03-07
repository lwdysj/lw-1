#! /usr/bin/python3 env
# -*- coding:utf-8 -*-'
'''
Created on 2019年3月6日

@author: liwei
'''
#爬取最好大学排行
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib.request
from mylog import MyLog
import re
import codecs
import random

class Item(object):
    paiming = None
    name = None
    address = None
    score = None

class GetMoive2018(object):
    def __init__(self):
        self.url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
        self.log = MyLog()
        self.items = self.spider()
        self.pipelines()
        
    def get_response(self):
        #获取页面信息
        flag = True
        ua = UserAgent()
        while flag:
            with open('new3proxy.txt', 'r') as fp:
                lines = fp.readlines()
                index = random.randint(1, len(lines))
                proxys = 'https://' + lines[index]
            
            fakeHeaders = {'User-Agent':ua.random}
            request = urllib.request.Request(self.url, headers=fakeHeaders)
                
            proxy = urllib.request.ProxyHandler({'https':proxys})
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)
        
            try:
                response = urllib.request.urlopen(request)
            except:
                flag = False
                self.log.error(u'导入URL: 失败')
            else:
                flag = True
                self.log.info(u'导入URL: 成功')
                return response
        
    def spider(self):
        #数据提取
        items = []
        response = self.get_response()
        soup = BeautifulSoup(response.read(), 'html.parser')
        datas = soup.find('div', {'class': 'news-text'}).find_all('tr')
        for data in datas[1:5]:
            item = Item()
            item.paihang = data.find_all('td')[0].text
            item.name = data.find_all('td')[1].text
            item.address = data.find_all('td')[2].text
            item.score = data.find_all('td')[3].text
            items.append(item)
            self.log.info(u'获取%s信息: 成功' % item.name)
        return items
    
    def pipelines(self):
        #数据清洗保存
        filename = 'daxuedata.txt'
        with codecs.open(filename, 'w', 'utf8') as fp:
            for item in self.items:
                fp.write('%d \t %s \t %s \t %.f \n' % (int(item.paihang), item.name, item.address, float(item.score)))
                self.log.info(u'%s保存至%s:成功' % (item.name, filename))

if __name__ == '__main__':
    GM = GetMoive2018()
