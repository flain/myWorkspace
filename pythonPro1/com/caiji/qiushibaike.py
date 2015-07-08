# -*- coding:utf-8 -*-

import urllib
import urllib2
import sys
from bs4 import BeautifulSoup
import re


url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, "Host": 'www.qiushibaike.com', "Accept-Language": 'zh-CN,zh;q=0.8,en;q=0.6'}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
html = response.read()
response.close()

# print type(page)
systype = sys.getfilesystemencoding()
# print sys.getfilesystemencoding()
# html = html.decode("UTF-8").encode(systype)
# html = unicode(html, "UTF-8").encode(systype)
soup = BeautifulSoup(html)
# print(soup)
html = soup.prettify()
# print(soup.select('div.content'))

pa = '<a.*?href="/users/.*?".*?>.*?src="(.*?)".*?>(.*?)</a>.*?class="content">(.*?)<.*?' \
     'class="stats-vote".*?class="number">(.*?)<.*?class="number">(.*?)</i>'
pattern = re.compile(pa, re.S)
items = re.findall(pattern, html)
print len(items)
for item in items:
    if not re.search('img', item[2]):
        print item[0], "\n", item[1].strip(), "\n内容：", item[2].strip(), "\n好笑:", item[3].strip(), "\n评论:", item[4].strip()
    else:
        print '有视频'
    newinput = raw_input()
    print(newinput)
    if input == "Q":
        break


