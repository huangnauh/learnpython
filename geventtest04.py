#!/usr/bin/env python
# coding: utf-8

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json
import time

def fetch(pid):
    response = urllib2.urlopen("http://www.w3schools.com/website/Customers_MYSQL.php")
    result = response.read()
    json_result = json.loads(result)
    for data in json_result:
        print("process %s: city:%s name:%s countary:%s" % (pid,data[u'City'],data[u'Name'],data[u'Country']))
    return json_result

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch,i))
    gevent.joinall(threads)

print('Synchronous:')
start = time.time()
synchronous()
print(time.time()-start)
print('Asynchronous:')
start = time.time()
asynchronous()
print(time.time()-start)
