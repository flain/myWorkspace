# coding:utf-8
__author__ = 'adminweke'

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    print 'method:', method
    print 'path:', path
    print environ['PATH_INFO']
    print environ['QUERY_STRING']
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
