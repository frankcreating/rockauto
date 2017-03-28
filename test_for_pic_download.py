#coding:utf-8
import requests
from bs4 import BeautifulSoup
import urllib2
import re
class Search_method(object):#several ways to get detailed information
	@classmethod
	def pic(self):
		f=open('/home/frank/fc333.txt')#text_name == partnum Beacuse I save text's name as partnum
		patten=re.compile(r"www.(.*?).jpg")#src="http://www.rockauto.com/info
		text=f.read()
		res=patten.findall(text)
		return res
	@staticmethod
	def pic_save(self):

if __name__ == '__main__':
	a=Search_method.pic()
	for i in a:
		print "www."+i+'.jpg'
