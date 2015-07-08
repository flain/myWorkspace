__author__ = 'adminweke'
import urllib2
import cookielib
import sys
from bs4 import BeautifulSoup
import re


filename ="312green.com2.txt"
cookie = cookielib.MozillaCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)


request = urllib2.Request("http://www.312green.com/office/changeinfo.php")

request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
request.add_header("User-Agent", "Mozilla5.0 (Windows NT 6.1) AppleWebKit537.36 (KHTML, like Gecko) Chrome41.0.2272.89 Safari537.36")
request.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
request.add_header("Referer", "http://www.312green.com/buy/detail-735932.html")


handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open(request)



html = response.read()
response.close()

soup = BeautifulSoup(html)
html = soup.prettify()
print html

print soup.select("input")



