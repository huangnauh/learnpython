import urllib2
import cookielib
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
response = opener.open('http://www.google.com')


def test1():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open('http://www.google.com')
    for item in cookie:
        print(item.name, item.value)


def test():
    handler = urllib2.FileHandler()
    request = urllib2.Request("file:/E:/code/huang/b/learnpy/files/1.txt")
    opener = urllib2.build_opener(handler)
    f = opener.open(request)
    print(f.read())
