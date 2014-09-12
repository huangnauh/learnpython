import hashlib,shelve,time,os
import http.cookies
import os.path
class Session:
    def __init__(self,expires=None,cookie_path=None):
        string_cookie = os.environ.get('HTTP_COOKIE','')
        self.cookie = http.cookies.SimpleCookie()
        self.cookie.load(string_cookie)
        if self.cookie.get('sid'):
            sid = self.cookie['sid'].values
            self.cookie.clear()
        else:
            self.cookie.clear()
            sid = hashlib.sha224(
                repr(time.time()).encode('ascii')
                        ).hexdigest()
        self.cookie['sid'] = sid
        if cookie_path:
            self.cookie['sid']['path'] = cookie_path
        session_dir = os.environ['PATH_TRANSLATED'] + "\\files"
        if not os.path.exists(session_dir):
            try:
                os.mkdir(session_dir)
            except OSError as e:
                raise
        self.session = shelve.open(session_dir + "\\sess_" + sid,writeback=True)
        if not self.session.get('cookie'):
            self.session['cookie'] = {'expires':''}
        self.set_expires(expires)
    def set_expires(self,expires=None):
        if not expires:
            self.session['cookie']['expires'] = ''
        elif isinstance(expires,int):
            self.session['cookie']['expires'] = expires
        self.cookie['sid']['expires'] = self.data['cookie']['expires']
    def close(self):
        self.session.close()
        