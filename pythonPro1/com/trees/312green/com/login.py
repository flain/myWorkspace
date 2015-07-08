__author__ = 'adminweke'
import urllib2
import cookielib
import urllib

data= {
    "username": "flain1",
    "password": "123789"
}
values= urllib.urlencode(data)

filename ="312green.com.txt"
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.312green.com/office/login.php?firstlogin=yes", values)
cookie.save(ignore_discard=True, ignore_expires=True)

print response.read()
