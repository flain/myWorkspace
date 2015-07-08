# coding:utf-8
__author__ = 'adminweke'

import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup
import proxyip
import random


def getSoup(url):
    request = urllib2.Request(url)
    request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    request.add_header("User-Agent", "Mozilla5.0 (Windows NT 6.1) AppleWebKit537.36 (KHTML, like Gecko) Chrome41.0.2272.89 Safari537.36")
    request.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
    request.add_header("Referer", "http://www.312green.com/buy/detail-735932.html")
    # handler = urllib2.HTTPCookieProcessor(cookie)
    # opener = urllib2.build_opener(handler)
    # response = opener.open(request)
    response = urllib2.urlopen(request)
    html = response.read()
    response.close()
    soup = BeautifulSoup(html)
    return soup


url = 'http://hehejun.312green.com/business-u38682-tqg-p1.html'
# soup = getSoup(url)
# print soup.prettify()



# proxy_support = urllib2.ProxyHandler(proxy_ip)
# proxydict = {}
# proxydict['http'] = "http://222.222.169.69:80"
# print proxydict
#
# proxy_support = urllib2.ProxyHandler({'http': "http://116.231.192.187:9999"})
# opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
# urllib2.install_opener(opener)
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)

handlers = [urllib2.ProxyHandler({'http': "http://116.231.192.187:9999"})]
opener = urllib2.build_opener(*handlers)
response = opener.open(urllib2.quote(url, safe=":/"), timeout=30)


html = response.read()
response.close()
soup = BeautifulSoup(html)
print soup.prettify()
