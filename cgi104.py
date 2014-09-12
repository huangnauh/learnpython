import hashlib,time,os
import http.cookies
cookie = http.cookies.SimpleCookie()
string_cookie = os.environ.get("HTTP_COOKIE")
def set_sid(cookie):
    sid = hashlib.sha224(repr(time.time()).encode('ascii')).hexdigest()
    cookie['sid'] = sid
    cookie['sid']['expires'] = 30 * 24 * 60 * 60
    return sid
if not string_cookie:
    sid = set_sid(cookie)
else:
    cookie.load(string_cookie)
    if 'sid' in cookie:
        sid = cookie['sid'].value
    else:
        sid = set_sid(cookie)

print(cookie)
print('Content-Type:text/html\n')
print('<html><body>')
print('<p>',cookie,'</p>')
for morsel in cookie:
    print('<p>',morsel,'=',cookie[morsel].value)
    print('<div style="margin:-1em auto auto 3em;">')
    for key in cookie[morsel]:
        print(key, '=', cookie[morsel][key], '<br />')
    print('</div></p>') 
if string_cookie:
    print('<p>Already existent session:%s</p>' % string_cookie)
print('<p>SID =', sid, '</p>')
print('</body></html>')