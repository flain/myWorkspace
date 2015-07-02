__author__ = 'adminweke'
import urllib2
import cookielib
import urllib

data= {"userName": "bbb", "password": "123123"}
values= urllib.urlencode(data)

filename ="16tripcookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.16trip.com/manage/index.jsp", values)
cookie.save(ignore_discard=True, ignore_expires=True)

print response.read()
