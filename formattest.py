import formatter
import htmllib
w = formatter.DumbWriter()
f = formatter.AbstractFormatter(w)
file = open("zhuoqiang.me\category\programming.html")
p = htmllib.HTMLParser(f)
p.feed(file.read())
p.close()
file.close()