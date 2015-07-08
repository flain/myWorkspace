# coding:utf-8
__author__ = 'adminweke'

import datetime,time


def writeline(txt):
    wfile = open("C:\\python.txt", 'a')
    wfile.writelines("\n")
    wfile.writelines(txt)
    wfile.flush()
    wfile.close()

# filename = "C:\\python.txt"
# wfile = open(filename, 'a')
# if not wfile.__exit__():
#     f = open(filename, 'w')
#     f.close()

# for i in range(2010, 2020):
#     date = str(i)+'-02-10'
#     if not date.__contains__('2015'):
#         print 'not'
#         continue
#     else:
#         print ' in else'


begin = '2015-07-01'
begin = time.strptime(begin, '%Y-%m-%d')
date = '2012-06-14'
date = time.strptime(date, '%Y-%m-%d')
print date > begin


