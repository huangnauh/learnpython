import hashlib,time,os,shelve
import http.cookies
cookie = http.cookies.SimpleCookie()
string_cookie = os.environ.get("HTTP_COOKIE")
if not string_cookie:
   sid = hashlib.sha224(repr(time.time()).encode('ascii')).hexdigest()
   cookie['sid'] = sid
   message = 'New session'
else:
   cookie.load(string_cookie)
   if 'sid' in cookie:
      sid = cookie['sid'].value
      message = 'already session'
   else:
      sid = hashlib.sha224(repr(time.time()).encode('ascii')).hexdigest()
      cookie['sid'] = sid
      message = 'New session'
cookie['sid']['expires'] = 60

session_dir = os.environ['PATH_TRANSLATED'] + "\\files"
session = shelve.open(session_dir + "\\sess_" + sid,writeback=True)
lastvisit = session.get('lastvisit')
if lastvisit:
    message += "Welcome back. Your last visit was at " + time.asctime(time.gmtime(float(lastvisit)))
session['lastvisit'] = repr(time.time())
session.close()
print("""\
%s
Content-Type: text/html\n
<html><body>
<p>%s</p>
<p>SID = %s</p>
</body></html>
""" % (cookie, message, sid))