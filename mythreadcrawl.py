信息抓取，用python,beautifulSoup,lxml,re,urllib2,urllib2去获取想要抽取的页面内容，然后使用lxml或者beautifulSoup进行解析，插入mysql 具体的内容，好了貌似很简单很easy的样子，可是里面的恶心之处就来了，第一，国内开发网站的人在指定网站编码或者是保存网站源码的时候并没有考虑什么编码，反正一句话，一个网站即使你用工具查看或者查看源码头信息查看到他们的源码是utf-8,或者GBK之类的，也别信，哎，什么东西信了就遭殃了，即<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

　　以下给出一些流程：（具体各个库不是我这里向说的哦）

　　import urllib2

　　 import chardet

　　html = urllib2.urlopen("某网站")

　  print chardet.detect(html) #这里会输出一个字典{'a':0.99999,'encoding':'utf-8'}

　　好，这整个html的编码都知道，该插入以utf-8建立的mysql数据库了吧，但是我就在插入的时候发生错误了，因为我使用lxml以后的字符串不是utf-8，而是Big5（繁体字编码）,还有各种未知编码EUC-JP(日本语编码)，OK，我采取了unicode方法，先对这个字段进行解码，在进行编码

if chardet.detect(name)['encoding'] == 'GB2312':
　　name = unicode(name,'GB2312','ignore').encode('utf-8','ignore')
elif chardet.detect(name)['encoding'] == 'Big5':
    name = unicode(name,'Big5','ignore').encode('utf-8','ignore')
elif chardet.detect(name)['encoding'] == 'ascii':
    name = unicode(name,'ascii','ignore').encode('utf-8','ignore')
elif chardet.detect(name)['encoding'] == 'GBK':
    name = unicode(name,'GBK','ignore').encode('utf-8','ignore')
elif chardet.detect(name)['encoding'] == 'EUC-JP':
    name = unicode(name,'EUC-JP','ignore').encode('utf-8','ignore')
else:
     name = '未知'

能有什么万用的方法没

github经常打不开，google经常打不开，stackoverflow经常打不开，readthedocs经常打不开，程序员还能好好查个资料



#源代码阅读# 开源软件项目在软件界的作用越来越重要，如何快速阅读源代码，领会其设计意图，把握其精髓，采取好方法相当关键。1.根据其使用手册了解其功能；2.采用好的反向工程工具获得其静态结构；3.借助架构模式和设计模式确定结构的关联关系；4.通过调试工具得到软件的动态特性；5.若有能力可重构
Rational 的Rose，Borland公司的Together等等
sagasw：这样的工具只有一个比较可用 understand 
这个软件名字就是understand 搜索能找到 比rose强出几条街


