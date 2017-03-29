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
	def __init__(self):
		partnum,oe_num=door.usr_wx()
		self.partnum=partnum
		self.oe_num=oe_num
		print 'start!'
		req=self.get_html()
		text=req.content
		self.text_save(partnum,text)
		finaltext=Search_method.bs(partnum)#use search method to find what we want 
		print finaltext
		print 'finish!and results already saved in local address%s'%partnum
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
	def text_save(self,name,text):#save $text(which you wanto save) as local text,name ==partnum
		with open('/home/frank/%s.txt'%name,'w+') as f:
			f.write(text)

	def text_read(self):#read text which save just a moment
		f=open('/home/frank/test.txt','r')
		tx=f.read()#return tx as final result
		if lambda:f is not None or f !='':
			print 'Yeah,we got something'
			f.close()
			return tx
		else:
			print 'it is totally empty!'
			f.close()
	def sql(self):
		x='123'
		return x


class door():
	@staticmethod
	def usr_wx():				#user operation interfaces

		print 'ready for searching oe?y/n?'
		a=raw_input()
		if a =='y' or a== 'yes':
			print 'what is file name you want to save in local file? partnum :'
			partnum=raw_input()
			print 'And input oe_num which you want to search:'
			oe_num=raw_input()
			return partnum,oe_num

		else:
			print 'USER EXIE!PROGRAM IS DONE!'
			return 0,0



'''
1st.call pic_search_url method and put in file_path and partnum
then make the result into pic_url_factory 
then call pic method and put in file_path and partnum
'''
class Search_method(object):#several ways to get detailed information
	@classmethod
	def pic_search_url(self,file_path,partnum):
		f=open(file_path+partnum+'.txt')#text_name == partnum Beacuse I save text's name as partnum
		patten=re.compile(r"www.(.*?).jpg")#src="http://www.rockauto.com/info
		text=f.read()
		pic_url=patten.findall(text)
		res=[i for i in range(len(pic_url))]
		n=0
		for i in pic_url:
			res[n]='http://www.'+i.replace('\\',"")+'.jpg'
			n+=1
		return res#http://www.rockauto.com/info/xxxxxxxxxxxxxxxxxxxxxxxx
	@classmethod
	def pic_save(self,pic_url,file_path,partnum):#save pic in file_path named partnum+1,2,4 or 5, and soon 
		n=0
		for i in pic_url:
			n+=1
			pic_name=file_path+'%s_%d'%(partnum,n)
				r=requests.get(i)
				with open(pic_name,'wb') as code:
					code.write(r.content)
					print 'picture already save in %s file_path'%file_path
				print i

if __name__=="__main__":
	a=swamp()#'fctext','0905038'
