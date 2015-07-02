__author__ = 'adminweke'
import urllib2
import cookielib
import urllib


filename ="16tripcookie.txt"
cookie = cookielib.MozillaCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)

request = urllib2.Request("http://www.16trip.com/manage/jsp/tour_list/dest.jsp")

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)
response = opener.open(request)


print response.read()
