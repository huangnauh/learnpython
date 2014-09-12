import hashlib,time,cgi,os
form = cgi.FieldStorage()
if 'sid' in form:
    message = 'Already existent session:'
    sid = form['sid'].value
else:
    sid = hashlib.sha224(repr(time.time()).encode('ascii')).hexdigest()
    message = 'New session'
print("""\
Content-Type: text/html\n
<html><body>
<p>%s</p>
<p>SID = %s</p>
<form method='post'>
<input type='hidden' name="sid" value="%s"/>
<input type='submit' value='submit'/>
</form>
<p><a href="./cgi105.py?sid=%s">reload</a></p>
""" % (message, sid, sid,sid,))

for i in os.environ:
    print('<p>',i,":",os.environ[i],"</p>")
print("</body></html>")