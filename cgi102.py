#!E:/python34/python.exe
import cgi,os
import cgitb
from ipdb import set_trace
cgitb.enable()
try:
    import msvcrt
    msvcrt.setmode(0,os.O_BINARY)
    msvcrt.setmode(1,os.O_BINARY)
except ImportError:
    pass
form = cgi.FieldStorage()
fileitem = form['file']
if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    f = open('files/'+fn,'wb',8192)
    nlen = 0
    nsum = 0
    while True:
        chunk = fileitem.file.read(8192)
        if not chunk:
            break
        f.write(chunk)
        nlen += len(chunk)
        nsum += 1
    f.close()
    
    message = 'the file "' + fn +'" was uploaded successfully'
else:
    message = 'no file'
print("Content-type: text/html\n")
print('<html><body>')
print("<title>Reply Page</title>")
print("<p> %s %s %s</p>" % (nlen,nsum,message))
print('</body></html>')
