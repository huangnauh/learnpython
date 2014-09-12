import urllib2
import urllib
import cookielib
import re
auth_url = 'http://www.nowamagic.net/'
home_url = 'http://www.nowamagic.net/'

data = {"username":"luoxia","password":"12345678"}
post_data = urllib.urlencode(data)
headers ={"Host":"www.nowamagic.net", "Referer":"http://www.nowamagic.net"}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req = urllib2.Request(auth_url,post_data,headers)
result = opener.open(req)
result = opener.open(home_url)
print result.read()


