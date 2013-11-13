# coding: utf-8
import requests
import re
from requests import *
import pyquery
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import sys
import os


reload(sys)
sys.setdefaultencoding('utf8')

import config
from config import *

##########################################################################

_list_org_urls=["人物 | People","观点 | View",    "本期专题：构建iOS持续集成平台 | Topic",
    "推荐文章 | Article", "特别专栏 | Column","避开那些坑 | Void","新品推荐 | Product"]

_urls={}
urls=[]
prod_urls=[]

for x in _list_org_urls:
    if x!='新品推荐 | Product':
        for y in org_urls[x]:
            _urls[y]=x
        urls+=org_urls[x]
    else:
        prod_urls=org_urls[x]


 
def prs(url,z):
	print 'begin requests%s'%url
	data=requests.get(url)
	print 'end requests%s'%url
	dd = unicode(data.content, "utf-8") 
	print 'begin match'
	#match_pre = re.findall(pattern_pre, dd)
	#print str(dd)
	d=pq(dd)
	match_pre=d.find('pre')
	print 'match pre done'
	#match_table = re.findall(pattern_table, dd)
	match_table=d.find('table')
	print 'match tab done'

	match_img=d.find('p>img')
	i=0
	ii=0
	iii=0
	import sys
	print sys.getdefaultencoding()
	for x in match_pre:
		print z,i
		f=open(base_folder+"one/%s-pre-%s.html"%(str(z),str(i)),'wb+')
		print pq(d(x)).encoding
		what=pq(d(x)).outerHtml().replace('&#13;','').replace('<pre>','<pre><code>').replace('</pre>','</code></pre>')
		f.write(u"<html><head>  <meta charset='utf-8'><link rel='stylesheet' href='default.min.css'><script src='highlight.pack.js'></script><script>hljs.initHighlightingOnLoad();</script></head><body>"+what+u"</body></html>")
		f.close()
		print 'end write begin praser'
		os.system("cd "+base_folder+"one;phantomjs c.js %s-pre-%s.html %s-pre-%s.png"%(str(z),str(i),str(z),str(i)))
		os.system("cd "+base_folder+"one;rm  %s-pre-%s.html g"%(str(z),str(i)))
		i+=1	
		print 'end pre%d'%i

	for x in match_table:
		if ii<=2:
			continue
		f=open(base_folder+"one/%d-table-%d.html"%(z,ii),'wb')
		f.write(u"<html><head>  <meta charset='utf-8'><link rel='stylesheet' href='default.min.css'><script src='highlight.pack.js'></script><script>hljs.initHighlightingOnLoad();</script><style>table{width:500px;}</style></head><body>"+pq(d(x)).outerHtml()+"</body></html>")
		f.close()
		os.system("cd "+base_folder+"one;phantomjs c.js %s-table-%s.html %s-table-%s.png"%(str(z),str(ii),str(z),str(ii)))
		os.system("cd "+base_folder+"one;rm %s-table-%s.html"%(str(z),str(ii)))
		ii+=1
		print 'end tab%d'%ii
	'''
	for x in match_img:
		_url = ('http://www.infoq.com/'+x.attrib['src'].split(';')[0])
		print _url
		_data = requests.get(_url)
		f=open(base_arch+"one/%d-img-%d.png"%(z,iii),'wb')
		f.write(_data.content)
		f.close()
		print 'end write img'
	'''

z=0
for  x  in urls:
	print x
	prs(x,z)
	z+=1