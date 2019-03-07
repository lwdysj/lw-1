#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2018年11月3日

@author: liwei
'''
#筛选可用代理ip

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
html = urlopen(url)
response = BeautifulSoup(html.read(), 'html.parser')

results = []
datas = response.find('div', {'class': 'news-text'}).find_all('tr')
for data in datas[1:5]:
    results.append([
        data.find_all('td')[0].text,
        data.find_all('td')[1].text,
        data.find_all('td')[2].text,
        data.find_all('td')[3].text
    ])
print(results)
