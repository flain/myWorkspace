import re
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# print html

soup = BeautifulSoup(html)
print soup.prettify()

print type(soup.title)
print 'soup.title=', soup.title

print type(soup.head)
print 'soup.head=', soup.head

print type(soup.a)
print 'soup.a=', soup.a

print type(soup.p)
print 'soup.p=', soup.p
print 'soup.p.name=', soup.p.name
print 'soup.p.attrs=', soup.p.attrs
print 'soup.p.attrs["class"]=', soup.p.attrs['class']
print 'soup.p.get("class")=', soup.p.get('class')
print 'soup.p.get("name")=', soup.p.get('name')
print '-------------------------------------------------'

print 'soup.p.string=', soup.p.string, type(soup.p.string)
print 'soup.a.string=', soup.a.string, type(soup.a.string)
print '-------------------------------------------------'

print soup.head.contents
print len(soup.body.contents)
print soup.body.contents

print soup.body.children
print "body 's children:"
i = 0
for tag in soup.body.children:
    print i, tag
    i = i+1

i = 0
for child in soup.descendants:
    print i, child
    i = i+1
