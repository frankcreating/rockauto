#coding:utf-8
import requests
import sys
import re
from bs4 import BeautifulSoup
class swamp(object):
	'''
	Query String Parameters
	view source
	view URL encoded
	partnum:123
	'''
	url='http://www.rockauto.com/en/partsearch/?'
	def __init__(self,partnum,oe_num):
		self.partnum=partnum
		self.oe_num=oe_num
		print 'start!'
		req=self.get_html()
		print req
		text=req.content
		self.text_save(partnum,text)
		print 'finish!'
	def get_html(self):
		print 'now loading Please wait for a moment!'
		url=self.url+'partnum='+self.oe_num
		req=requests.get(url)
		print 'already visited %s'%url
		check=lambda req:req.status_code==200#check if success;
		if check(req):
			return req
		else:
			print "False,renturn code is %s"%req.status_code
 
	def pic_save():
		pass
	def text_save(self,name,text):#save $text(which you wanto save) as local text
		with open('/home/frank/%s.txt'%name,'w+') as f:
			f.write(text)

	def text_read(self):#read text which save just a moment
		f=open('/home/frank/test.txt','r')
		tx=f.read()
		if lambda:f is not None or f !='':
			print 'Yeah,we got something'
			f.close()
			return tx
		else:
			f.close()
	def sql(self):
		x='123'
		return x
	def usr_wx():
		print 'continue for searching oe?y/n?'
		a=input()
		if a =='y' or a== 'yes':
			print 'what is file name you want to save?partnum :'
			partnum=input()
			print 'input oe_num:'
			oe_num=input()


class Search_method(object):#several ways to get detailed information
	def bs(text_name):
		soup=BeautifulSoup(open('/home/frank/%s.txt'%text_name),'html5lib')#text_name == partnum Beacuse I save text's name as partnum
		res=soup.findAll('span',{"title":"Replaces these Alternate/ OE Part Numbers"})
		return res
	def web_source(self):
		pass
	def img_source(self):
		pass


if __name__=="__main__":
	a=swamp('fctext','0905038')
