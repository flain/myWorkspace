# -*- coding:utf-8 -*-
#图片采集实例

import urllib
import urllib2
import re

imageURL ='http://gtd.alicdn.com/sns_logo/i4/TB1Qz2_IXXXXXXvXXXXSutbFXXX.jpg_60x60.jpg'
fileName = 'mm1.jpg'
u = urllib.urlopen(imageURL)
data = u.read()
f = open(fileName, 'wb')
f.write(data)
f.close()
