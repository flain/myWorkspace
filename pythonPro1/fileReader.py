# coding:utf-8
__author__ = 'adminweke'


for line in open("C:\\ccp.log", 'r'):
    if len(line.strip()) > 0:
        if 'outer_code' in line:
            items = line.split(' ')
            print items
            print items[0], items[1]
