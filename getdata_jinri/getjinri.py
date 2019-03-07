#! /usr/bin/python3 env
# -*- coding:utf-8 -*-'

'''
Created on 2018年10月16日

@author: liwei
'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from mylog import MyLog
import time, os

class Item(object):
    image_url = None

class GetData(object):
    def __init__(self):
        self.url = 'https://www.toutiao.com/search/?keyword=\xe8\xa1\x97\xe5\xa4\xb4\xe7\xaf\xae\xe7\x90\x83'
        self.log = MyLog()
#        self.urls = self.get_urls()
        self.items = self.spider()
        self.pipelines()
        
#    def get_urls(self):
#        pass
       
    def get_html(self):
        driver = webdriver.PhantomJS()
        driver.get(self.url)
        driver.implicitly_wait(10)
        submitelement = driver.find_element_by_xpath('//div[@class="tabBar"]//li[@class="y-left tab-item "]')
        submitelement.click()
        time.sleep(5)
        pageSource = driver.page_source
        self.log.info(u'successful')
        return pageSource
    
    def spider(self):
        i = 1
        items = []
#        for url in self.urls:
#        response = self.get_response()
        pageSource = self.get_html()
        try:
            soup = BeautifulSoup(pageSource, 'html.parser')
            datas = soup.find_all('div', {'class': 'articleCard'})
            for data in datas:
                item = Item()
                try:
                    item.image_url = data.find('a', {'class': 'img-wrap'}).find('img', {'alt': ''})['src']
                    items.append(item)
                except KeyError:
                    pass
                self.log.info(u'获取信息: 成功')
        except AttributeError:
            self.log.info(u'url None')
        return items
    
    def pipelines(self):
        filename = '街头篮球1'
        if os.path.exists(filename):
            os.chdir(filename)
        else:
            os.mkdir(filename)
            os.chdir(filename)
        i = 1
        for url in self.items:
            with open(str(i) + '.jpg', 'wb') as fp:
                i += 1
                pic = requests.get(url.image_url)
                fp.write(pic.content)

if __name__ == '__main__':
    GM = GetData()
