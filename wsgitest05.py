#!E:/python34/python.exe
from wsgiref.simple_server import make_server
import re
import cgi
import traceback
import sys



def index(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b"This is the home page,more function in /hello!"]
 
def say_hello(environ,start_response):
    args=environ['myapp.url_args']
    if args:
        subject=cgi.escape(args[0])
    else:
        subject="world"
    start_response('200 OK',[('Content-Type','text/html')])
    response_body = '''Hello %(subject)s!''' % {'subject': subject}
    return [response_body.encode('utf-8')]
 
def not_found(environ,start_response):
    start_response('404 NOT FOUND',[('Content-Type','text/html')])
    return [b'Sorry,no page here!']

urls = [
        (r'^$',index),
        (r'hello/?$',say_hello),
        (r'hello/(.+)$',say_hello)
        ]
        
def myapp(environ,start_response):
    path = environ.get("PATH_INFO",'').lstrip('/') 
    for regex,callback in urls:
        match = re.search(regex,path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ,start_response)
    return not_found(environ,start_response)
    
class ExceptionMiddleware:
    def __init__(self,app):
        self.app = app
    def __call__(self,environ,start_response):
        appiter = None
        try:
            appiter = self.app(environ,start_response)
            for item in appiter:
                yield item
        except:
            e_type,e_value,tb = sys.exc_info()
            Apptraceback = ['Traceback(most recent call last):']
            Apptraceback += traceback.format_tb(tb)
            try:
                start_response('500 INTERNAL SERVER ERROR',[('Content-Type','text/html')])
            except:
                pass
            yield '<br/>'.join(Apptraceback)
        if hasattr(appiter,'close'):
            appiter.close()
            
if __name__=='__main__':
    from wsgiref.simple_server import make_server
    myapp=ExceptionMiddleware(myapp)
    srv=make_server('localhost',8080,myapp)
    srv.serve_forever()