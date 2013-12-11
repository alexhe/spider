#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-  
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
print sys.getdefaultencoding()
import config
from config import *

##########################################################################

_list_org_urls=["人物 | People","观点 | View",    "本期专题：内核那些事 | Topic",
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



html_ = u"""
<html>
    <head>
        <link rel='stylesheet' href='../style/default.min.css'><script src='../style/highlight.pack.js'></script>
        <link rel="stylesheet" href="../style/print.css"/>
        <script>hljs.initHighlightingOnLoad();</script>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
         <div class="page">
            <div class="head">
                <h1>{head}</h1>
            </div>
            <div class="title">
                <h1>{title}</h1>
            </div>
            <div class="author">
                {author}
            </div>
            {content}

            <div class="orglink">
                <p>
                    <strong>原文链接：<a href="{org}">{org}</a></strong>
                </p>
                <div>
                    {likes}
                </div>
            </div>
         </div>
    </body>
</html>"""


def get_rec(title, path, ids):
    data = requests.post(
        'http://www.infoq.com/api/recommendationlinks.action', {"topicIds": ids,
                                                                "title": title, "contentPath": path, "language": 'zh'
                                                                })
    import json
    _d = json.loads(data.content)
    return "".join('<li><a href="%s">%s</a></li>' % (x['url'], x['title']) for x in _d[1:] )


def get_article_content(url):
    data = requests.get(url)
    d = pq(data.content)
    pattern_pre = '{"topicIds": "(.*)", "title"'
    match_pre = re.findall(pattern_pre, data.content)
    match_img=d.find('p > img')
    title = d('title').text()
    print '    '+str(title)
    author = d('.author_general').outerHtml().replace('href="/cn/author',
                                                      'href="http://infoq.com/cn/author').replace('<em>|</em>', '').replace('<em>/</em>', '')[:-72]
    content = d('.text_info_article').remove('.comments_like').remove('a[rel="permalink"]').remove('script').remove('.h1-r').remove('.related_sponsors').remove('.random_links').remove('.comment_here').remove('.comments').remove('.all_comments').remove(
        '#overlay_comments').remove('.related_sponsors').remove('#replyPopup').remove('#editCommentPopup').remove('#responseContent').remove('#messagePopup').remove('.related_sponsors').outerHtml().replace('src="/resource', 'src="http://www.infoq.com/resource').replace('<pre>','<pre><code>').replace('</pre>','</code></pre>')
    for x in match_img:
        _url = pq(d(x)).attr('src')
        if _url is '' or _url is None:
            continue
        print _url
        file_name = _url.replace('/','-').replace('http:--infoqstatic.com-resource',base_arch+'one').replace('one-','one/')
        content=content.replace(_url,file_name.replace(base_arch,''))
        _data = requests.get(_url)
        with open(file_name,'wb') as f:
            f.write(_data.content)
            f.close()
        print 'end write img'
    likes = ''
    try:
        likes = get_rec(title, url.replace(
            'http://infoq.com/cn', ''), match_pre[0])
        likes = ("<strong>相关内容</strong><ul>" + likes + "</ul>")
    except Exception, e:
        likes = ""
        print e

    return html_.format(head=_urls[url], title=title, author=author, content=content, likes=likes, org=url).encode('utf-8')


def get_news_content(url):
    data = requests.get(url)

    _data = data.content
    d = pq(_data)
    pattern_pre = '{"topicIds": "(.*)", "title"'
    _de_pattern = '发布于[\s\S]*<em>\|</em>'
    match_pre = re.findall(pattern_pre, _data)
    title = d('title').text()
    match_img=d.find('p > img')
    print '    '+str(title)
    author = d('.author_general').outerHtml().replace('href="/cn/author',
                                                      'href="http://infoq.com/cn/author').replace('<em>|</em>', '').replace('<em>/</em>', '')[:-60]

    content = d('.text_info').remove('.comments_like').remove('a[rel="permalink"]').remove('script').remove('.h1-r').remove('.related_sponsors').remove('.random_links').remove('.comment_here').remove('.comments').remove('.all_comments').remove(
        '#overlay_comments').remove('.related_sponsors').remove('#replyPopup').remove('#editCommentPopup').remove('#responseContent').remove('#messagePopup').remove('.related_sponsors').outerHtml().replace('src="/resource', 'src="http://www.infoq.com/resource').replace('<pre>','<pre><code>').replace('</pre>','</code></pre>')
    for x in match_img:
        _url = pq(d(x)).attr('src')
        if _url is '' or _url is None:
            continue
        print _url
        file_name = _url.replace('/','-').replace('http:--infoqstatic.com-resource',base_arch+'one').replace('one-','one/')
        content.replace(_url,file_name)
        _data = requests.get(_url)
        with open(file_name,'wb') as f:
            f.write(_data.content)
            f.close()
        print 'end write img'
    likes = ''
    try:
        likes = get_rec(title, url.replace(
            'http://infoq.com/cn', ''), match_pre[0])
        likes = ("<strong>相关内容</strong><ul>" + likes + "</ul>")
    except Exception, e:
        print e
        likes = ""

    zz= html_.format(head=_urls[url], title=title, author=author, content=content, likes=likes, org=url)
    print type(zz)
    return zz
def get_title(url):
    data = requests.get(url)
    _data = data.content
    d = pq(_data)
    title = d('title').text()
    print str(title)
    return title
# 获取
def get_prod_content(url):
    html__='''
        <div class="title">
                <h2>{title}</h2>
            </div>
            <div class="author">
                {author}
            </div>
            {content}
            <div class="orglink">
                <p>
                    <strong>原文链接：<a href="{org}">{org}</a></strong>
                </p>

            </div>
    '''
    data = requests.get(url)
    d = pq(data.content)
    description = d('meta[name="description"]').attr('content')

    title = d('title').text()
    print '    '+str(title)
    author = d('.author_general').outerHtml().replace('href="/cn/author',
                                                      'href="http://infoq.com/cn/author').replace('<em>|</em>', '').replace('<em>/</em>', '')[:-60]

    return html__.format( title=title, author=("<br6/>" + author), content=("<br/><p>" + description + "</p>"), org=url)

def gen_plant():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <link rel="stylesheet" href="../style/plant.css"/>

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      
    </head>
    <body>
         <div class="page">
            <div class="head">
                <h1>封面植物 </h1>
            </div>
            <div class="title">
                <h1>{plant_name}</h1>
            </div>
           
            <div class="text_info text_info_article">
                <p>
                <img style="max-width:200px;margin:5px;" src="../res/{plant_img}"/>{plant_desc}</p>                
                
            </div>
            </div>
            </body>
    """
    print '封面植物生成'
    with open(base_arch+'plant.html','w+') as f:
        f.write(html.format(plant_name=plant_name,plant_desc=plant_desc,plant_img=plant_img))

def gen_editor():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <link rel="stylesheet" href="../style/plant.css"/>

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      
    </head>
    <body>
         <div class="page">
            <div class="head">
                <h1>推荐编辑 | {recommand_editor_name} </h1>
            </div>
          
            <div class="text_info text_info_article">
                <p>
                <img style="max-width:200px;" src="../res/{recommand_editor_img}"/>{recommand_editor_desc}</p>                
                
            </div>
            </div>
            </body>
    """
    print '推荐编辑生成'
    with open(base_arch+'editor.html','w+') as f:
        f.write(html.format(recommand_editor_name=recommand_editor_name,recommand_editor_img=recommand_editor_img,recommand_editor_desc=recommand_editor_desc))



# 写入架构师的html文件

def gen_content():
    i = 0
    import codecs
    for x in urls:
        with codecs.open(base_arch+"%d.html" % i, 'w+','utf-8') as f:
            if x.find('/news/') > 0:
                f.write(get_news_content(x))
            if x.find('/article') > 0:
                f.write(get_article_content(x))
            i += 1

# 写入架构师的新品推荐内容html文件
    with open(base_arch+"%d.html" % i, 'w+') as f:
        z = '''
        <html>
        <head>
    
            <link rel="stylesheet" href="../style/print.css"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        </head>
        <body>
             <div class="page">
                <div class="head">
                    <h1>新品推荐 | Product</h1>
                </div>
               '''
    
        for x in prod_urls:
            z += get_prod_content(x)
        f.write(z+           '''
             </div></body></html>''')
    i += 1
def gen_toc():
    with open(base_arch+'toc.html','w+') as f:
        html__='''
        <html>
        <head>
    
            <link rel="stylesheet" href="../style/print.css"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
                  img{
                    float: left;
                    margin-right: 8px;
                    margin-bottom: 5px；
                }
                           h1, h4{    color: rgb(24,103,45);                margin-bottom: 9px;                            -webkit-margin-before: 0.4em;

    }
    
                p{
    
                    margin: 0px;
                    line-height: 1.5;
                }
            </style>
        </head>
        <body>
             <div class="page">
                    <div class="toc" style="text-align: center;"><h1>目录</h1></div>'''
    
        for x in _list_org_urls:
            print x

            html__+=('<h4>'+x+'</h4>')
            for y in org_urls[x]:
                html__+=('<p>'+get_title(y)+'</p>')
        f.write(html__)
def gen_toc_for_kindle():
    with open(base_arch+'toc_kindle.html','w+') as f:
        html__='''
        <html>
        <head>
    
            <link rel="stylesheet" href="../style/print.css"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
                  img{
                    float: left;
                    margin-right: 8px;
                    margin-bottom: 5px；
                }
                           h1, h4{    color: rgb(24,103,45);                margin-bottom: 9px;                            -webkit-margin-before: 0.4em;

    }
    
                p{
    
                    margin: 0px;
                    line-height: 1.5;
                }
            </style>
        </head>
        <body>
             <div class="page">
                    <div class="toc" style="text-align: center;"><h1>目录</h1></div>'''
        ii =0 
        for x in _list_org_urls:
            print x

            html__+=('<h4>'+x+'</h4>')
            for y in org_urls[x]:

                html__+=('<p><a href="'+str(ii)+'.html">'+get_title(y)+'</a></p>')
                if x=='新品推荐 | Product':
                    ii+=0
                else:
                    ii+=1
        f.write(html__)
def gen_foreword():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                   
    </head>
    <body>
         <div class="page" >
            <div class="head">
                <h1>卷首语 </h1>
            </div>
                <h1>{foreword_title}</h1>
           
            <div class="" style="-webkit-margin-before: 0em;">
               {forword_content}
            </div>
                
                        <div class="author">
                        本期主编：{chief_editor}
                    </div>
            </div>
            </body>
    """
    print '卷首语生成'
    with open(base_arch+'foreword.html','w+') as f:
        f.write(html.format(forword_content=forword_content,foreword_title=foreword_title,chief_editor=chief_editor))
def gen_topic():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    </head>
    <body>
         <div class="page" >
            <div class="head">
                <h1>专题推荐语 </h1>
            </div>
                <h1>{topic_title}</h1>
           
            <div class="" style="-webkit-margin-before: 0em;">
               {topic_desc}
               
            </div>
              <img src="../res/{topic_image}" style="width:500px;margin:0 auto;"/>  
            </div>
            </body>
    """
    print '推荐语生成'
    with open(base_arch+'topic.html','w+') as f:
        f.write(html.format(topic_title=topic_title,topic_desc=topic_desc,topic_image=topic_image))
def gen_column():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    </head>
    <body>
         <div class="page" >
            <div class="head">
                <h1>推荐语 </h1>
            </div>
                <h1>{column_title}</h1>
           
            <div class="" style="-webkit-margin-before: 0em;">
               {column_desc}
            </div>
                 <img src="../res/{column_image}" style="width:500px;margin:0 auto;" />  
            </div>
            </body>
    """
    print '推荐语生成'
    with open(base_arch+'column.html','w+') as f:
        f.write(html.format(column_title=column_title,column_desc=column_desc,column_image=column_image))
def gen_right():
    html='''
    <!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Untitled Document</title>
        <link rel="stylesheet" href="../style/copyright.css"/>

</head>

<body>
<div style="width:600px;margin:0 auto;height:100%;" >
<table>
        <tbody>
            <tr>
            <td>
                    <img width="200px" src="../res/250.png"/>
              </td>
              <td width="400px"  valign="top">
              <div style="margin-left:20px">
               <h1>架构师 {which_month} 月刊</h1>
        <small>每月8日出刊</small>
        <br/>
        <p>本期主编：{chief_editor}<br/>
        美术/流程编辑：水羽哲<br/>
        总编辑：霍泰稳<br/>
        发行人：霍泰稳</p>
        <p>读者反馈：editors@cn.infoq.com<br/>
        投稿：editors@cn.infoq.com<br/>
        商务合作：sales@cn.infoq.com <br/>
        InfoQ 中文站：<a href="http://weibo.com/infoqchina">新浪微博</a></p>
</div>
              </td>
                
              <td>
              </td>
                 
           </tr>
        </tbody>
    </table>

    
    <table style="">
        <tr>
            <td>
            <img width="100px" src="../res/{chief_editor_image}"/>
            </td>
            
            <td width="20px"></td>
            <td valign="top" style="margin-top:0px;">
            <h3>本期主编：{chief_editor}</h3>
              <p style="font-size:13px;">{chief_editor_desc}</p>
            </td>
        </tr>
    </table>
    
    
    <table style="margin-top:150px;bottom:0px;margin-left:auto;margin-right:auto;">
    <tr>
    <td>
    <img width="100px" src="http://cdn1.infoq.com/styles/i/logo_bigger.jpg" />
    </td>
    <td valign="top">
     <p>《架构师》月刊由InfoQ 中文站出品。</p>
        
        <p>所有内容版权均属 C4Media Inc.所有，未经许可不得转载。</p>
    </td>
    </tr>
    </table>
</div>
</body>
</html>

    '''
    print '版权页生成'
    with open(base_arch+'right.html','w+') as f:
        f.write(html.format(which_month=which_month,chief_editor=chief_editor,chief_editor_desc=chief_editor_desc,chief_editor_image=chief_editor_image))
def gen_cover():
    html='''
    <!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Untitled Document</title>
        <link rel="stylesheet" href="../style/cover.css"/>


</head>

<body>
<img src="../res/cheader.png" width="794px">

<table style="margin:0 auto;border:none; ">
<tr valign="top">
<td valign="top"  width="300px">
<table width="100%" border="none" >
<tr>
<td valign="top" style="font-size:140px;color:#3d69a8;">
架构</td>
</tr>
<tr>
<td valign="top"  style="font-size:35px;color:black;">
{which_month}月 ARCHITECT</td>
</tr>
</table>
</td>
<td valign="top"  style='font-size:200px;color:#69a364;'>
师
</td>
</tr>
</table>

<div  style="margin-top:40px;">
</div>

<table>
    <tr>
        <td width="400px">
           <div class="tupian" style="background:url(../res/{plant_img})   no-repeat  fixed 00px   ;overflow:visible;width:400px;height:500px;
"></div>
        </td>
        <td width="20px"></td>
        <td width="400px" valign="top">
            <table width="100%">
                <tr><td valign="top">
                    <h3>
                    特别专题
                    </h3>
                    {_topic}
                    <hr/>
                    {_column}
                    <hr/>
                    {_tvjm}
                </td></tr>
            </table>
        </td>
    </tr>
</table>


<div width="794px" style="margin-top:40px">
<img src="../res/cfooter.png"   width="794px">
</div>
</body>
</html>
'''
    print '首页生成'

    _topic='<h4>'+topic_title+'</h4>'
    for x in org_urls['本期专题：'+topic_title+' | Topic']:
            _topic+=('<h5>'+get_title(x)+'</h5>')

    _column='<h4>'+column_title+'</h4>'
    for x in org_urls['特别专栏 | Column']:
            _column+=('<h5>'+get_title(x)+'</h5>')

    _tvjm=''
    for x in org_urls['推荐文章 | Article']:
            _tvjm+=('<h5>'+get_title(x)+'</h5>')

    with open(base_arch+'cover.html','w+') as f:
        f.write(html.format(which_month=which_month,_topic=_topic,_column=_column,_tvjm=_tvjm,plant_img=plant_img))


######################################################################
#gen_foreword()
#gen_toc()
gen_toc_for_kindle()
#gen_topic()
#gen_column()
#gen_plant()
#gen_editor()
#gen_content()
#gen_right()
#gen_cover()