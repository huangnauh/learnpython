# coding=utf-8
import codecs
s = "中文测试" + u"Chinese".encode('utf-8')
print s.decode('utf-8')
with open("E:/code/huang/b/learnpy/venv/code/test.txt",'r') as f:
    content = f.read()
    if content[:3] == codecs.BOM_UTF8:
        content = content[3:]
    print content.decode('utf-8').encode('gbk')


#with open("E:/code/huang/b/learnpy/venv/code/test.txt",'r') as f:
#	print f.read().decode('utf-8').encode('gbk')