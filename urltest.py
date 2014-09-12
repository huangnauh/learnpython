import urllib2
import urlparse
LOGIN = '123zifeiyu@163.com'
PASSWD = 'xiuluochan'
URL = 'http://www.163.com/'

def handler_version(url):
	print "handler_version"
	hdlr = urllib2.HTTPBasicAuthHandler()
	hdlr.add_password(None,url,LOGIN,PASSWD)
	opener = urllib2.build_opener(hdlr)
	urllib2.install_opener(opener)
	return url

def request_version(url):
	print "request_version"
	from base64 import encodestring
	req = urllib2.Request(url)
	b64str = encodestring("%s:%s" % (LOGIN,PASSWD))[:-1]
	req.add_header("Authorization", "Basic %s" % b64str)
	return req

for funcType in ('handler','request'):
	print '*** Using %s:' % funcType.upper() 
	url = eval('%s_version' % funcType)(URL)
	f = urllib2.urlopen(url)
	print f.readline()
	print f.readline()
	f.close()
	
def get_unread_msgs(user, passwd):
    auth = urllib2.HTTPBasicAuthHandler()
    auth.add_password(
            realm='New mail feed',
            uri='https://mail.google.com',
            user='%s'%user,
            passwd=passwd
            )
    opener = urllib2.build_opener(auth)
    urllib2.install_opener(opener)
    try:
        feed= urllib2.urlopen('https://mail.google.com/mail/feed/atom')
        return feed.read()
    except urllib2.HTTPError, e:
        if e.code == 401:
            print "authorization failed"            
        else:
            raise e # or do something else
    except: #A general except clause is discouraged, I let it in because you had it already
        return None