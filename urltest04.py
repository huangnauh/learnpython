
import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib
import urllib2
import httplib
import os.path

class MyHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        return self.do_open(MyHTTPConnection, req)

class MyHTTPConnection(httplib.HTTPConnection):
    debuglevel = 1
    def send(self, data):
        """Send `data' to the server."""
        if self.sock is None:
            if self.auto_open:
                self.connect()
            else:
                raise NotConnected()

        if self.debuglevel > 0:
            print "send:", repr(data)
        blocksize = 8192
        if hasattr(data,'next'):
            print("--sending an iterable")
            for datablock in data:
                self.sock.sendall(datablock)
            print("--end sending an iterable")
        elif hasattr(data,'read') and not isinstance(data, array):
            if self.debuglevel > 0: print "sendIng a read()able"
            datablock = data.read(blocksize)
            while datablock:
                self.sock.sendall(datablock)
                datablock = data.read(blocksize)
        else:
            self.sock.sendall(data)
        return
            
class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return
    
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return
    
    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Add the form fields
        parts.extend(
            [ part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              '',
              value,
            ]
            for name, value in self.form_fields
            )
        
        # Add the files to upload
        parts.extend(
            [ part_boundary,
              'Content-Disposition: file; name="%s"; filename="%s"' % \
                 (field_name, filename),
              'Content-Type: %s' % content_type,
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )
        
        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)    
        
class FileForm(object):
    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary
    def add_field(self,name,value):
        self.form_fields.append((name,value))
    def add_file(self,fieldname,filename,mimetype=None):
        part_boundary = '--' + self.boundary
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        part=[
                part_boundary,
                'Content-Disposition: file; name="%s"; filename="%s"' %  \
                (fieldname,filename),
                'Content-Type: %s' % mimetype,
                '',
                '',
            ]
        data = '\r\n'.join(part)
        self.files.append((data,filename))
    def getdata(self):
        blocksize = 8192
        for data, filename in self.files:
            yield data
            fileobj=open(filename,'rb')
            while True:
                datablock = fileobj.read(blocksize)
                if datablock:
                    yield datablock
                else:
                    yield '\r\n'
                    break
        bodyend = "--" +self.boundary + "--"+'\r\n';
        yield bodyend
    def getContentLength(self):
        length = 0
        for data, filename in self.files:
            length += len(data) + os.path.getsize(filename)+len('\r\n')
        bodyend = "--" +self.boundary + "--"+'\r\n';
        return length + len(bodyend)
        
                
            
def test():
    form = FileForm()
    #form.add_field('first','Doug')
    #form.add_field('lastname','huang')
    form.add_file('file', 'Back.jpg')
    #form.add_file('math', 'math.html', 
    #              fileHandle=StringIO('Python math should be learned.'))
    request = urllib2.Request('http://localhost:8888/cgi-bin/cgi104.py')
    request.add_header('User-agent','huanglibo')
    request.add_header('Content-type',form.get_content_type())
    request.add_header('Content-length',form.getContentLength())
    request.add_data(form.getdata())
    opener = urllib2.build_opener(MyHTTPHandler)
    response = opener.open(request)
    print("********************")
    print(request.get_data())
    print("********************")
    print(response.read())

if __name__ == '__main__':
    test()
def test1():
    # Create the form with simple fields
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')
    # Add a fake file
    form.add_file('biography', 'bio.txt', 
                  fileHandle=StringIO('Python developer and blogger.'))

    # Build the request
    request = urllib2.Request('http://localhost:8888/')
    request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')
    body = str(form)
    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print 'OUTGOING DATA:'
    print request.get_data()

    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()


        
                
                
                
        
            