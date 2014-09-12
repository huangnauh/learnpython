#!E:/python34/python.exe
#import urllib.request
import urllib2
import urllib
query_args = { 'q':'query string', 'foo':'bar' }
encoded = urllib.urlencode(query_args)
print('111111',encoded)
request = urllib2.Request("http://localhost:8080")
request.add_header('User-agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
request.add_data(encoded)
print "2222",request.get_data()
response = urllib2.urlopen(request)
data = response.read()
print data



