#!/usr/bin/env python
# coding: utf-8

from gevent.wsgi import WSGIServer
from gevent.queue import Queue,Empty
import simplejson as json
def application(environ,start_response):
    status = "200 OK"
    headers = [
            ("Content-Type",'text/html')]
    start_response(status,headers)
    yield "<p>hello"
    yield "world</p>"
WSGIServer(('127.0.0.1',8000),application).serve_forever()
