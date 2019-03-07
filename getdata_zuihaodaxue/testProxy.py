#! /usr/bin/python3 env
# -*- coding:utf-8 -*-

'''
Created on 2018年10月16日

@author: liwei
'''

import urllib.request
import threading
from fake_useragent import UserAgent

class TestProxy(object):
    def __init__(self):
        self.rfile = 'proxy.txt'
        self.wfile = 'new3proxy.txt'
        self.threads = 10
        self.alivelist = []
        self.get_links()
        self.save_proxy()
        
    def save_proxy(self):
        with open(self.wfile, 'a') as fp:
            for alive in self.alivelist:
                fp.write(alive + '\n')
        
    def get_links(self):
        with open(self.rfile, 'r') as fp:
            lines = fp.readlines()
            line = lines.pop()
            while lines:
                for i in range(self.threads):
                    t = threading.Thread(target=self.getAliveProxy, args=(line, ))
                    t.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue
            
    def getAliveProxy(self, line):
        flag = True
        ua = UserAgent()
        url = 'http://zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
        while flag:
            fakeHeaders = {'User-Agent':ua.random}
            request = urllib.request.Request(url, headers=fakeHeaders)
            
            proxys = 'http://' + line
            handler = urllib.request.ProxyHandler({'http':proxys}) 
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)
            try:
                response = urllib.request.urlopen(request)
            except: 
                print('proxy error')
                return
            else:
                self.alivelist.append(line)
                print(line)
                print('proxy true')
               
if __name__ == '__main__':
    TP = TestProxy()
    print('ending...')