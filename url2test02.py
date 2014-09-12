#coding=utf-8
import urllib2
import urllib
import cookielib
import Cookie
import os.path
import sqlite3
import os
import base64
import win32crypt
def testsave():
    data={"email":"huanglibo2010@gmail.com","password":"xiuluochang"}
    post_data=urllib.urlencode(data)
    cookie = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    header = ("User-agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1")
    req = urllib2.Request("http://www.renren.com/PLogin.do")
    req.add_header(*header)
    req.add_data(post_data)
    opener.open(req)
    cookie.save("E:/code/huang/b/learnpy/files/"+"Cookies1",True)
def testload():
    cookie = cookielib.MozillaCookieJar()
    cookie.load("E:/code/huang/b/learnpy/files/"+"Cookies1",True)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    header = ("User-agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1")
    req = urllib2.Request("http://www.renren.com/PLogin.do")
    req.add_header(*header)
    content = opener.open(req)
    f = open("E:/code/huang/b/learnpy/files/test1.html",'wb')
    f.write(content.read())
    f.close()
def sqlite3_load(domain=None):
#os.environ["LOCALAPPDATA"]
    cookie_file_path = os.path.join("E:/code/huang/b/learnpy/files/Cookies")
    if not os.path.exists(cookie_file_path):
        raise Exception(cookie_file_path,"is not cookie file")
    cookiejar = cookielib.CookieJar()
    conn = sqlite3.connect(cookie_file_path)
    sql = "select host_key,name,encrypted_value,path from cookies"
    if domain:
        sql += ' where host_key like "%{}%"'.format(domain)
    print(sql)
    for row in conn.execute(sql):
        pwdHash = str(row[2])
        try:
            ret = win32crypt.CryptUnprotectData(pwdHash, None, None, None, 0)
        except:
            print 'Fail to decrypt chrome cookies'
        print(ret[1])
        cookie_item = cookielib.Cookie(
            version=0, name=row[1], value=ret[1],
                     port=None, port_specified=None,
                     domain=row[0], domain_specified=None, domain_initial_dot=None,
                     path=row[3], path_specified=None,
                     secure=None,
                     expires=None,
                     discard=None,
                     comment=None,
                     comment_url=None,
                     rest=None,
                     rfc2109=False)
        cookiejar.set_cookie(cookie_item)
    conn.close()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    req = urllib2.Request("http://www.renren.com/")
    header = ("User-agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1")
    req.add_header(*header)
    content = opener.open(req)
    f = open("E:/code/huang/b/learnpy/files/test2.html",'wb')
    f.write(content.read())
    f.close()

#testsave()
#testload()
sqlite3_load("renren.com")