#!/usr/bin/env python3
# coding: utf-8
import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding='utf-8'
		return r.text
	except:
		return "Error"

def get_content(url):
	comments=[]
	html=get_html(url)
	soup=BeautifulSoup(html,'lxml')
	liTags=soup.find_all('li',attrs={'class':' j_thread_list thread_top j_thread_list clearfix'})

	for li in liTags:
		comment={}
#		comment['title']=li.find('a',attrs={'class':'j_th_tit '}).text.strip()
#		comment['link']='http://tieba.baidu.com/'+li.find('a',attrs={'class':'j_th_tit '})['href']
#		comment['name']=li.find('span',attrs={'class':'tb_icon_auther '}).text.strip()
		comment['time']=li.find('span',attrs={'class':'pull-right is_show_create_time '})
		comments.append(comment)
	return comments
	

def output(dict):
	with open('/home/liwei/li-1.txt','a+') as f:
		for comment in dict:
			f.write('时间:{} \n'.format(comment['time']))
	print('当前页面已爬玩')

def main(base_url,deep):
	url_list=[]
	for i in range(0,deep):
		url_list.append(base_url+'&pn='+str(50*i))
	for url in url_list:
		content=get_content(url)   
		output(content)
	
base_url='http://tieba.baidu.com/f?kw=生活大爆炸&ie=utf-8'
deep=3

if __name__=='__main__':
	main(base_url,deep)

