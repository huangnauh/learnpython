import urllib
"""
b'Host: 127.0.0.1:8888\r\n'
b'Connection: keep-alive\r\n'
b'Content-Length: 30395\r\n'
b'Cache-Control: max-age=0\r\n'
b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q
=0.8\r\n'
b'Origin: http://127.0.0.1:8888\r\n'
b'User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko
) Chrome/36.0.1985.125 Safari/537.36\r\n'
b'Referer: http://127.0.0.1:8888/cgi101.html\r\n'
b'Accept-Encoding: gzip,deflate,sdch\r\n'
b'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4\r\n'
b'\r\n'
"""
query_args = {'age':'20<html>=100', 'hobbies':['software','tunning']}
qs = urllib.urlencode(query_args,doseq=True)
response = urllib.urlopen("http://127.0.0.1:8888/cgi-bin/cgi103.py",qs)
print(response.read())






