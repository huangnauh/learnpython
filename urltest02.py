#!E:/python34/python.exe
#import urllib.request
import urllib2
import urllib
query_args = { 'q':'query string', 'foo':'bar' }
encoded = urllib.urlencode(query_args)
print(encoded)
response = urllib2.urlopen('http://localhost:8888/?',encoded)

print('response:',response)
print('response.geturl:',response.geturl())
print('response.getcode:',response.getcode())
headers = response.info()
print('DATE    :', headers['date'])
print('response.info:',headers,str(type(headers)))
for line in response:
    print line.rstrip()




