import socketserver,re,cgi,io
import urllib.parse
import wsgiref.simple_server
class AppException(Exception):
    pass
class Request:
    def __init__(self,env):
        self.env = env
        self.wsgi_input = env.get('wsgi.input')
        self.methed = env['REQUEST_METHOD']
        self.attrs = {}
        self.attributes = {}
        self.encoding = "UTF-8"
    def __getattr__(self,attr):
        if attr == "params" and "params" not in self.attrs :
            if self.method == "POST"
                self.form = cgi.FieldStorage(fp=self.wsgi_input,
                            envrion=self.env,keep_blank_values=1)
                self.params = {}
                for key in self.fs:
                    self.params[key] = self.fs[key].values
                self.attrs["params"] = self.params
        return self.attrs[attr]
    
class Response:
    def __init__(self,start_response,write=None):
        self.encoding="UTF-8"
        self.start_response = start_response
        self._write = write
    def write(self,bytes):
        if self._write is None:
            self._write = self.start_response("200 OK",[
                    ("Content-type","text/html;charset="+self.encoding),
                    ])
        self._write(bytes)
    def redirect(self,url):
        if self._write is not None:
            raise AppException("writing can't redirect")
        self.start_response("302 OK",
                [("Location",url)]

class WSGIAppication:
    def __init__(self,urls=None):
        self.urls = urls
    def getHandlerByUrls(self,url):
        url = url.replace("//","/")
        urlArr = url.split("/")
        for setUrl in self.urls:
            setUrlArr = setUrl.split('/')
            if len(setUrlArr) == len(urlArr):
                for i in range(len(urlArr)):
                    if (i == len(urlArr) - 1 and 
                    (setUrlArr[i] == '*' or setUrlArr[i] == urlArr[i] or  
                        ('*' in setUrlArr[i] and re.search(setUrlArr[i].replace("*",r'\w*'),urlArr[i])))):
                        return self.urls[setUrl]
                    if setUrlArr[i] == '*' or setUrlArr[i]==' ' :
                        continue
                    if setUrlArr[i] != urlArr[i] :
                        break
                        
    def make_app(self):
        def wsgi_app(env,start_response):
            url = env["PATH_INFO"]
            handlerCls = self.getHandlerByUrl(url)
            if handlerCls is None:
                start_response("500 OK", [("Content-type","text/html;charset=utf-8")])
                return ["Error Url"]
            if not hasattr(handlerCls,"do_GET") and not hasattr(handlerCls,"do_POST")):
                start_response("500 OK", [("Content-type","text/html;charset=utf-8")])
                return ["Error Mapping"]
            resquest = Request(env)
            response = Response(start_response)
            try:
                handler = handlerCls(request, response)
            except TypeError as e:
                handler = handlerCls()
            methodname = "do_" + request.method
            result = None
            try:
                result = getattr(handler,methodname)(request, response)
            except TypeError as e:
                result = getattr(handler,methodname)()
            if result is None:
                result = []
            return result
        return wsgi_app
    def make_server(self,serverIp='',port=8000,test=False):
        from wsgiref.simple_server import make_server
        from wsgiref.simple_server import 
        httpd = make_server(serverIp, port, self.make_app(), server_class=WSGIServer)  
        if test:
            httpd.handle_request()
        else:
            httpd.serve_forever()
        return True
class TestHandler:  
    def __init__(self):  
        pass  
    def do_GET(self, request=None, response=None):  
        response.write(b"Hello")  
    def do_POST(self, request=None, response=None):  
        #request.encoding='UTF-8'  
        #response.write(request.params["name"])  
        response.redirect("/a/x")
        
def main():  
    app = WSGIApplication(urls={"/a/*":TestHandler, "/a/b/*.do":TestHandler})  
    app.make_server(test=True) 
if __name__=="__main__":  
    main()