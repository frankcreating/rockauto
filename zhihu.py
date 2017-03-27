#coding:utf-8
import requests
import sys
class swamp(object):
	'''
	Query String Parameters
	view source
	view URL encoded
	partnum:123

	'''
	url='http://www.rockauto.com/en/partsearch'
	def __init__(self,partnum,oe_num):
		self.partnum=partnum
		self.oe_num=oe_num
		print 'start!'
		print req
	def clmb(self):
		value={
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
		'Host':'www.rockauto.com',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'oe_num':'%s'%self.oe_num
		}

		print 'now is climbing-->'+self.url
		req=requests.post(self.url,value)
		check=lambda req:req.status_code==200
		if check(req):
			return req
		else:
			print "False"
	def pic_save():
		pass
	def text_save(self,text):#save
		with open('/home/frank/test2.txt','w+') as f:
			f.write(self.text)

	def text_read(self):#read
		f=open('/home/frank/test.txt','r')
		tx=f.read()
		if lambda:f is not None or f !='':
			print 'Yeah,we got something'
			f.close()
			return tx
		else:
			f.close()
	def search_txt():
		part='(.*?)'
	def sql(self):
		x='123'
		return x
	def usr_wx():
		pass


if __name__=="__main__":
	a=swamp(123,int('0905039'))
