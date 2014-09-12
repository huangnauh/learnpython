#!E:/python34/python.exe
from wsgiref.simple_server import make_server
from http.cookies import SimpleCookie
import cgi
import re
import hashlib,time
html = """
<html>
<body>
   <form enctype="multipart/form-data" method="post" action="">
        <p>File:<input type='file' name='file'></p>
        <input type="submit" name="submit" value="upload"/>  
   </form>
   <p>%s
   </p>
   <p>%s
   </p>
   <p>%s
   </p>
</body>
</html>"""
def application(environ,start_response):
    try:
        request_body_size = remainbytes = int(environ.get('CONTENT_LENGTH',0))
    except ValueError:
        request_body_size = remainbytes = 0
    if remainbytes > 0:
        CONTENT_TYPE = environ.get('CONTENT_TYPE','')
        boundary = re.findall('multipart/form-data.*boundary=(.*)',CONTENT_TYPE)[0].encode('ascii')
        wsgi_input = environ['wsgi.input']
        line = wsgi_input.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False,"Content NOT begin with boundary")
        line = wsgi_input.readline()
        remainbytes -= len(line)
        line = line.decode('ascii')
        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line)[0]
        line = wsgi_input.readline()
        remainbytes -= len(line)
        line = wsgi_input.readline()
        remainbytes -= len(line)
        blocksize = 8192
        out = open(fn,'wb')
        preline = wsgi_input.readline()
        remainbytes -= len(line)
        while remainbytes > 0:
            line = wsgi_input.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith(b'\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                break
            else:
                out.write(preline)
                preline = line
    cookie = SimpleCookie(environ.get('HTTP_COOKIE',''))
    if 'sid' in cookie:
        sid = cookie['sid'].value
        message = 'already session'
    else:
        sid = hashlib.sha224(repr(time.time()).encode('ascii')).hexdigest()
        cookie['sid'] = sid
        message = 'new session'
    cookie['sid']['expires'] = 60
    response_body = html % ("OK" if request_body_size else "Empty",message,sid)
    status = '200 OK'
    response_headers = [('Set-Cookie',cookie.output(header="")),
                ('Content-Type','text/html'),
                ('Content-Length',str(len(response_body)))
                ]
    start_response(status,response_headers)
    #response_body = response_body.encode('ascii')
    return [response_body.encode('ascii')]
    
http = make_server(
    'localhost',
    8888,
    application
    )
http.serve_forever()