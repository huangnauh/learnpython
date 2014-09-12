#!E:/python34/python.exe
import cgi, os
import cgitb
import time
import http.cookies
cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()


# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
   while True:
      chunk = f.read(chunk_size)
      if not chunk: break
      yield chunk
      
# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   f = open('files/' + fn, 'wb', 10000)

   # Read the file in chunks
   for chunk in fbuffer(fileitem.file):
      f.write(chunk)
   f.close()
   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'
cookie = http.cookies.SimpleCookie()
cookie['lastvisit'] = str(time.time())
cookie['lastvisit']['expires'] = 30 * 24 * 60 * 60
cookie['lastvisit']['path'] = '/cgin-bin/'
cookie['lastvisit']['comment'] = 'holds the last user\'s visit date'
cookie['lastvisit']['domain'] = 'localhost'
cookie['lastvisit']['max-age'] = 30 * 24 * 60 * 60
cookie['lastvisit']['secure'] = ''
cookie['lastvisit']['version'] = 1
#print('Set-Cookie: lastvisit=' + str(time.time())) 
 
print("Content-Type: text/html\n")
print('<p>',cookie,'</p>')
for morsel in cookie:
    print('<p>',morsel,'=',cookie[morsel].value)
    print('<div style="margin:-1em auto auto 3em;">')
    for key in cookie[morsel]:
        print(key, '=', cookie[morsel][key], '<br />')
    print('</div></p>') 
print("<html><body>")
print('<p>Server time is', time.asctime(time.localtime()), '</p>')
cookie_string = os.environ.get('HTTP_COOKIE')
if not cookie_string:
    print('<p>First visit or cookies disabled</p>')
else:
    print('<p>The returned cookie string was "' + cookie_string + '"</p>')
cookie.load(cookie_string)
last_visit = float(cookie['lastvisit'].value)
print('<p>Your last visit was at',time.asctime(time.localtime(last_visit)),'</p>')
print("""<p>%s</p>
</body></html>
""" % (message,))