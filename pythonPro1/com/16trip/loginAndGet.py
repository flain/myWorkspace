__author__ = 'adminweke'
import urllib2
import cookielib
import urllib
from bs4 import BeautifulSoup

data= {"userName": "bbb", "password": "123123"}
values= urllib.urlencode(data)

filename ="16tripcookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.16trip.com/manage/index.jsp", values)
cookie.save(ignore_discard=True, ignore_expires=True)

afterLoginUrl = 'http://www.16trip.com/manage/jsp/tour_list/dest.jsp'
result = opener.open(afterLoginUrl)

# print result.read()
html = result.read()
soup = BeautifulSoup(html)
soupHtml = soup.prettify()
print soupHtml

with open('16trip1.html', 'w') as f:
    f.write(html)

# with open('16trip2.html', 'w') as f1:
#     f1.write(soupHtml)
