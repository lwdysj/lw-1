'''
Created on 2018年10月15日

@author: liwei
'''
#! /usr/bin/python3 env
# -*- coding: utf-8 -*-

import getpass
import sys
import logging

#创建一个自用的log
class MyLog(object):
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        log_filename = sys.argv[0][0:-3] + '.log'
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        #将日志显示在屏幕上并输出到日志文件内
        logHand = logging.FileHandler(log_filename)
        logHand.setFormatter(formatter)
        logHand.setLevel(logging.ERROR)

        logHandst = logging.StreamHandler()
        logHandst.setFormatter(formatter)
        
        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandst)

    #日志的5个级别对应下面函数
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)
        
    def critical(self, msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug('I am debug')
    mylog.info('I am info')
    mylog.warn('I am warn')
    mylog.error('I am error')
    mylog.critical('I am critical')


