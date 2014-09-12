import urllib
import cookielib
#coding=utf-8
import urllib2
import os

login_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
postdata = {'from': 'web', 'submit': '\xe7\x99\xbb \xe5\xbd\x95', 'done': 'http://www.xiami.com', '_xiamitoken': '0bc24d8321dd9a67b58ad3c65dbe20a0', 'password': 'xiuluochang', 'email': 'huanglibo2010@gmail.com'}
path = os.getcwd()
print(path)
postdata = urllib.urlencode(postdata)
cookie = cookielib.MozillaCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
print("Logging...")
req = urllib2.Request(url='http://www.xiami.com/member/login', data=postdata, headers=login_header)
response = opener.open(req)
f = open(path+ "/login.html",'wb')
f.write(response.read())
f.close()
cookie.save(path+"/Cookies",True)


signin_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', 'X-Requested-With':'XMLHttpRequest', 'Content-Length':0, 'Origin':'http://www.xiami.com', 'Referer':'http://www.xiami.com/'}
print 'signing...'
req = urllib2.Request(url='http://www.xiami.com/task/signin', data='', headers=signin_header)
response = opener.open(req)
f = open(path+ "/signin.html",'wb')
f.write(response.read())
f.close()
cookie.save(path+"/Cookies1",True)
