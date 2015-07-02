# coding=utf-8
import urllib
import urllib2
import cookielib

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()
# value={"name": "liu", "password": "ddd"}
# data=urllib.urlencode(value)
# print data
#
#
# url= "http://www.xxxxx.net/cqcre"
# request = urllib2.Request(url)
# try:
#     response = urllib2.urlopen(request, timeout=3)
# except urllib2.HTTPError as e:
#     print 'error', e.reason
#     print e.code
# except urllib2.URLError as e:
#     print 'urlerror', e.reason
# else:
#     print "OK"

# cookie = cookielib.CookieJar()
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.16trip.com/manage/")
for c in cookie:
    print c.name, '=', c.value
cookie.save(ignore_discard=True, ignore_expires=True)
