#coding=utf-8
__author__ = 'huanglibo'

"""Miscellaneous utility functions"""

import urllib2
import urlparse
import gzip
import StringIO
from weakref import WeakKeyDictionary

USER_AGENT = 'OpenAnything/1.0 +http://diveintopython.org/http_web_services/'

class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        return result

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
        result.status = code
        return result


class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, hdrs):
        result = urllib2.HTTPDefaultErrorHandler.http_error_default(self, req, fp, code, msg,hdrs)
        result.status = code
        return result




def openAnything(source, etag=None, lastmodified=None, agent=USER_AGENT):
    if hasattr(source, "read"):
        return source

    if source == '-':
        import sys
        return sys.stdin

    if urlparse.urlparse(source)[0] == "http":
        request = urllib2.Request(source)
        request.add_header("User-Agent",agent)
        if etag:
            request.add_header("If-None-Match",etag)
        if lastmodified:
            request.add_header("If-Modified-Since",lastmodified)
        request.add_header("Accept-encoding","gzip")
        opener = urllib2.build_opener(SmartRedirectHandler)
        return opener.open(request)

        # try to open with native open function (if source is pathname)
    try:
        return open(source)
    except (IOError, OSError):
        pass

        # treat source as string
    return StringIO.StringIO(str(source))

def fetch(source, etag=None, last_modified=None, agent=USER_AGENT):
    result = {}
    f = openAnything(source,etag,last_modified,agent)
    result['data'] = f.read()
    if hasattr(f,'headers'):
        result['etag'] = f.headers.get('ETag')
        result['lastmodified'] = f.headers.get('Last-Modified')
        if f.headers.get('content-encoding', '') == 'gzip':
            result['data'] = gzip.GzipFile(fileobj=StringIO.StringIO(result['data'])).read()
    if hasattr(f,'url'):
        result['url'] = f.url
        result['status'] = 200
    if hasattr(f,'status'):
        result['status'] = f.status
    f.close()
    return result


class MyTestProperty(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print "in getter"
        return self.__name

    @name.setter
    def name(self,name):
        print "in setter"
        self.__name = name

    @name.deleter
    def name(self):
        print "in deleter"
        del self.__name

    age = property(fget = lambda o : o.__age,fset = lambda o,v : setattr(o,"__age",v),fdel=lambda o : delattr(o,"__age"))


class Descriptor(object):
    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        print "****",instance
        if instance is None:
            return self
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        for callback in self.callbacks.get(instance, []):
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)

class Foo(object):
    balance = Descriptor(0)

def warning(value):
    if value < 100:
        print "warning"

class Descriptor1(object):
    def __init__(self, name, default=None):
        self.default = default
        self.name = '_'+name
        self.protocols = []

    def __get__(self, instance, owner):
        if not instance:
            return self
        return getattr(instance,self.name,self.default)

    def __set__(self, instance, value):
        for protocol in self.protocols:
            meth = getattr(instance,"%s_callback" % protocol,None)
            if meth:
                print meth.__name__
                meth(value)           #why
        setattr(instance,self.name,value)
    def add_callback(self, myclass, callback):
        meth = callback.func_name
        i = meth.find('_')
        protocol = meth[:i]
        self.protocols.append(protocol)
        setattr(myclass,callback.func_name,callback)  #为什么不行

class BAR1(object):
    name = Descriptor1("name",24)

def value_callback(self,value):
    if value < 100:
        print "warning"

def foooooo():
    abc1 = BAR1()
    BAR1.name.add_callback(BAR1,value_callback)
    abc2 = BAR1()
    abc1.name = 30


class MyRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self,req,fp,code,msg,headers):
        print "$$$$$$$$"
        print headers
        print "#################################in http_error_301"
        result = urllib2.HTTPRedirectHandler.http_error_301(self,req,fp,code,msg,headers)
        result.status = code
        return result
    def http_error_302(self,req,fp,code,msg,headers):
        print "$$$$$$$$"
        print headers
        print "#################################in http_error_302"
        result = urllib2.HTTPRedirectHandler.http_error_302(self,req,fp,code,msg,headers)
        result.status = code
        return result

class ErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self,req,fp,code,msg,headers):
        print "$$$$$$$$"
        print headers
        print "################################# in http_error_default"
        result = urllib2.HTTPError(req.get_full_url(),code,msg,headers,fp)
        result.status = code
        return result


import footest
import time
class Bar(object):
    def __del__(self):
        time.sleep(5)
        footest.cleanup()

if __name__ == "__main__":
    pass


def testdebug():
    debughandler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener(debughandler,ErrorHandler(),MyRedirectHandler())
    request = urllib2.Request("http://www.google.com")
    request.add_header('Accept-encoding', 'gzip')
    f = opener.open(request)


def testProperty():
    c = MyTestProperty('huang',25)
    x = c.name
    c.name = 'yujia'
    print c.name
    del c.name
    x = c.age
    c.age = 24
    del c.age
    print c.age