# coding:utf-8
__author__ = 'adminweke'
from urllib2 import urlopen

import urllib2
from bs4 import BeautifulSoup

enable_proxy = True

# proxy_handler = urllib2.ProxyHandler({"http": 'http://58.246.96.211:8080'})
# proxy_handler = urllib2.ProxyHandler({"http": 'http://183.224.1.30:80'})
proxy_handler = urllib2.ProxyHandler({"http": '112.84.130.26:10000'})


null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)
#设置代理end

header = {'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3','User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}

#Debug Log star

# httpHandler = urllib2.HTTPHandler(debuglevel=1)
#
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#
# opener = urllib2.build_opener(httpHandler, httpsHandler)
#
# urllib2.install_opener(opener)

#Debug Log end
url = 'http://hehejun.312green.com/business-u38682-tqg-p1.html'
request = urllib2.Request(url, headers= header)

res = urlopen(request, timeout=8000)
html = res.read()
soup = BeautifulSoup(html)
res.close()
print soup.prettify()
