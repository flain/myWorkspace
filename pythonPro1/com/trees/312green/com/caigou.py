# coding:utf-8
__author__ = 'adminweke'
import urllib2

import cookielib
import sys
from bs4 import BeautifulSoup
import re
import datetime,time

reload(sys)
sys.setdefaultencoding("utf-8")

filename ="312green.com2.txt"
cookie = cookielib.MozillaCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)


def getSoup(url):
    request = urllib2.Request(url)
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
    return soup

def readUser(uid):
    url = "http://a.312green.com/business-u" + uid + "-tqg-p1.html"
    soup = getSoup(url)
    # html = soup.prettify()
    if len(soup.select("div.itembox")) > 0:
        print "user:", uid, "have data"
        wfile = open("C:\\python.txt", 'a')
        # wfile.writelines("\n=============================================================================begin:"+uid)
        i = 1
        for item in soup.select("div.itembox"):
            date = item.select(".date")[0].get_text()
            if(not checkDate(date)):
                continue
            title = item.select("h2")[0].getText()
            content = (item.select("div.itemcontent")[0].get_text()).strip()
            # print i,"=", date, title, content
            wfile.writelines("\n" + date + "\n" + title + "\n" + content)
            wfile.writelines("\n-------------------------------------------------------------")
            wfile.flush()
            i = i+1

        if(i>1):
            wfile.writelines(getUserByUid(uid))
            wfile.writelines("\n=============================================================================end"+uid)
        else:
            print 'user:', uid, "is no date in time"

        wfile.close()
    else:
        print "user:", uid, "no data"

#检查时间是否符合要求
def checkDate(dateTime):
    begin = '2015-07-01'
    begin = time.strptime(begin, '%Y-%m-%d')
    date = time.strptime(dateTime, '%Y-%m-%d')
    return date > begin

#拿到用户资料
def getUserByUid(uid):
    url = "http://hehejun.312green.com/linkmode-u" + uid + ".html"
    soup = getSoup(url)
    infos = soup.select("div.twocol")[0].select("li")
    r = ''
    for t in infos:
        r = r + t.get_text().strip()+"\n"
    return r



# getUserByUid("38682")

for i in range(1000, 10000, 1):
    try:
        readUser(str(i))
    except urllib2.URLError, e:
        print "urllib2.URLError in user:", i









