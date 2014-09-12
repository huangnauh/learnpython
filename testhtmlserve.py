#!E:/python34/python.exe
#encoding=utf-8
import http.server
import socket
import re,platform
import io,os,time
import urllib.parse
import cgi
import sys

def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
 
def modification_date(filename):
    # t = os.path.getmtime(filename)
    # return datetime.datetime.fromtimestamp(t)
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getmtime(filename)))
    
class FileHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).
 
        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().
 
        """
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        r = []
        displaypath = cgi.escape(urllib.parse.unquote(self.path))
        r.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        r.append("<html>\n<title>Directory listing for %s</title>\n" % displaypath)
        r.append("<body>\n<h2>Directory listing for %s</h2>\n" % displaypath)
        r.append("<hr>\n")
        r.append("<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
        r.append("<input name=\"file\" type=\"file\"/>")
        r.append("<input type=\"submit\" value=\"upload\"/>")
        r.append("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp")
        r.append("<input type=\"button\" value=\"HomePage\" onClick=\"location='/'\">")
        r.append("</form>\n")
        r.append("<hr>\n<ul>\n")
        for name in list:
            fullname = os.path.join(path, name)
            colorName = displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                colorName = '<span style="background-color: #CEFFCE;">' + name + '/</span>'
                displayname = name
                linkname = name + "/"
            if os.path.islink(fullname):
                colorName = '<span style="background-color: #FFBFFF;">' + name + '@</span>'
                displayname = name
                # Note: a link to a directory displays with @ and links with /
            filename = os.getcwd() + '/' + displaypath + displayname
            r.append('<table><tr><td width="60%%"><a href="%s">%s</a></td><td width="20%%">%s</td><td width="20%%">%s</td></tr>\n'
                    % (urllib.parse.quote(linkname), colorName,
                        sizeof_fmt(os.path.getsize(filename)), modification_date(filename)))
        r.append("</table>\n<hr>\n</body>\n</html>\n")
        encoded = "".join(r).encode('ascii')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return f
        
    def do_POST(self):
        r,info = self.deal_post_data()
        print(r,info,"by:",self.client_address)
        f = io.BytesIO()
        rlist = []
        
        rlist.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        rlist.append("<html>\n<title>Upload Result Page</title>\n")
        rlist.append("<body>\n<h2>Upload Result Page</h2>\n")
        rlist.append("<hr>\n")
        if r:
            rlist.append("<strong>Success:</strong>")
        else:
            rlist.append("<strong>Failed:</strong>")
        rlist.append(info)
        rlist.append("<br><a href=\"%s\">back</a>" % self.headers['referer'])
        rlist.append("<hr><small>Powered By: bones7456, check new version at ")
        rlist.append("<a href=\"http://li2z.cn/?s=SimpleHTTPServerWithUpload\">")
        rlist.append("here</a>.</small></body>\n</html>\n")
        encoded = "".join(rlist).encode('ascii')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        print(f.read())
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        if f:
            self.copyfile(f,self.wfile)
            f.close()
            
    def deal_post_data(self):
        boundary = self.headers.get_boundary()
        print("boundary:",boundary)
        boundary = boundary.encode('ascii')
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False,"Content NOT begin with boundary")
        line = self.rfile.readline()
        remainbytes -= len(line)
        line = line.decode('ascii')
        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line)
        if not fn:
            return (False,"Can't find out file name...")
        path = self.translate_path(self.path)
        osType = platform.system()
        try:
            if osType == 'Linux':
                fn = os.path.join(path, fn[0].decode('gbk').encode('utf-8'))
            else:
                fn = os.path.join(path,fn[0])
        except Exception as e:
            return (False, "文件名请不要用中文，或者使用IE上传中文名的文件。")
        while os.path.exists(fn):
            fn += '_'
        line = self.rfile.readline()
        print("11111",line)
        remainbytes -= len(line)
        line = self.rfile.readline()
        print("22222",line)
        remainbytes -= len(line)
        try:
            out = open(fn,'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?")
        preline = self.rfile.readline()
        remainbytes -= len(line)
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith(b'\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, "File '%s' upload success!" % fn)
            else:
                out.write(preline)
                preline = line
        return (False, "Unexpect Ends of data.")
        
                
            

httpd = http.server.HTTPServer(
            ('127.0.0.1',8765),
            FileHTTPRequestHandler
            )
host, port = httpd.socket.getsockname()[:2]
name = socket.getfqdn(host)
sa = httpd.socket.getsockname()
print(name,host,port)
print("Serving HTTP on", sa[0],"port",sa[1],"...")          
httpd.serve_forever()
