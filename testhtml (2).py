#coding= utf-8
__author__ = 'huanglibo'

""" HTML 规范要求所有非 HTML (像客户端的 JavaScript ) 必须包括在 HTML 注释中
 但不是所有的页面都是这么做的 (而且所有的最新的浏览器也都容许不这样做).
 如果脚本包含了小于和等于号，SGMLParser 可能会错误地认为找到了标记和属性。
 SGMLParser 总是把标记名和属性名转换成小写，这样可能破坏了脚本
 并且 BaseHTMLProcessor 总是用双引号来将属性封闭起来 (尽管原始的 HTML 文档可能使用单引号或没有引号) ，这样必然会破坏脚本。
 应该总是将您的客户端脚本放在 HTML 注释中进行保护"""


"""
触发时机:
• __getattr__: 访问不存在的成员。
• __setattr__: 对任何成员的赋值操作。
• __delattr__: 删除成员操作。
• __getattribute__: 访问任何存在或不存在的成员，包括 __dict__。
不要在这⼏个⽅法⾥直接访问对象成员，也不要⽤ hasattr/getattr/setattr/delattr 函数，因为它
们会被再次拦截，形成⽆限循环。正确的做法是直接操作 __dict__。
⽽ __getattribute__ 连 __dict__ 都会拦截，只能⽤基类的 __getattribute__ 返回结果。
class A(object):
    def __init__(self, x):
        self.x = x! ! ! ! # 会被 __setattr__ 捕获。

    def __getattr__(self, name):
        print "get:", name
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        print "set:", name, value
        self.__dict__[name] = value

    def __delattr__(self, name):
        print "del:", name
        self.__dict__.pop(name, None)

    def __getattribute__(self, name):
        print "attribute:", name
        return object.__getattribute__(self, name)
"""


"""
类型和实例各⾃拥有⾃⼰的名字空间。
访问对象成员时，就从这⼏个名字空间中查找，⽽⾮以往的 globals locals
instance.__dict__ -> class.__dict__ -> baseclass.__dict__

实例字段存储在 instance.__dict__，代表单个对象实体的状态
静态字段存储在 class.__dict__，为所有同类型实例共享
必须通过类型和实例对象才能访问字段
以双下划线开头的 class 和 instance 成员视为私有，会被重命名

所有基类的实例字段都存储在 instance.__dict__ 外，其他成员依然是各归各家。

而属性以装饰器或描述符实现
不同于前⾯提过的对象成员查找规则，属性总是⽐同名实例字段优先
"""

"""
通过inspect.stack()可以获得一个堆栈列表。
堆栈列表的第一个元素表示当前执行的位置，最后一个元素表示最外层的调用。
列表中的每个元素都是一个六个元素的元组：(frame对象, 文件名, 当前行号, 函数名, 保存相关源代码行的列表, 当前行在源代码列表中的位置)。
"""

"""
名字作⽤域是在编译时确定的
如果函数中包含 exec 语句，编译器⽣成的名字指令会依照 LEGB 规则搜索
解释器会将 locals 名字复制到 FAST 区域来优化访问速度，因此直接修改 locals 名字空间并不会影响该区域。
在底层表示frame对象的C语言结构体中，还存在一个f_localsplus字段，它是一个数组，存取数组要比存取字典高效得多。
Python虚拟机使用f_localsplus数组保存局域变量，并在需要的时候使它和f_locals字典保持同步。

编译期作⽤域不受执⾏期条件影响。
"""
import htmllib
import formatter
import string
import sgmllib
import cgi
import sys
import string
import formatter
import cStringIO
import htmlentitydefs
import re
import xml.dom.minidom
import getopt
import random

_debug = 0


class NoSourceError(Exception): pass


class KantGenerator:
    def __init__(self):
        self.loadGrammar(grammar)
        self.loadSource(source and source or self.getDefaultSource())
        self.refresh()

    def _load(self, source):
        sock = toolbox.openAnything(source)
        xmldoc = xml.dom.minidom.parse(sock).documentElement
        sock.close()
        return xmldoc

    def loadGrammar(self,grammar):
        self.grammar = self._load(grammar)
        self.refs = {}
        for ref in self.grammar.getElementsByTagName("ref"):
            self.refs[ref.attributes["id"].value] = ref


    def loadSource(self, source):
        self.source = self._load(source)

    def getDefaultSource(self):
        xrefs = []
        for xref in self.grammar.getElementsByTagName("xref"):
            xrefs.append(xref.attributes["id"].value)
        standaloneXrefs = [e for e in self.refs if e not in xrefs]
        if not standaloneXrefs:
            raise NoSourceError, "can't guess source, and no source specified"
        return '<xref id="%s"/>' % random.choice(standaloneXrefs)

    def reset(self):
        self.pieces = []
        self.capitalizeNextWord = 0

    def refresh(self):
        self.reset()
        self.parse(self.source)
        return self.output()

    def output(self):
        return "".join(self.pieces)

    def randomChildElement(self, node):
        choices = [e for e in node.childNodes if e.nodeType == e.ELEMENT_NODE]
        chosen = random.choice(choices)
        if _debug:
            sys.stderr.write('%s available choices: %s\n' % \
                             (len(choices), [e.toxml() for e in choices]))
            sys.stderr.write('Chosen: %s\n' % chosen.toxml())
        return chosen

    def parse(self, node):
        parseMethod = getattr(self,"parse_%s" % node.__class__.__name__)
        parseMethod(node)

    def parse_Document(self, node):
        self.parse(node.documentElement)

    def parse_Text(self, node):
        """parse a text node

        The text of a text node is usually added to the output buffer
        verbatim.  The one exception is that <p class='sentence'> sets
        a flag to capitalize the first letter of the next word.  If
        that flag is set, we capitalize the text and reset the flag.
        """
        text = node.data
        if self.capitalizeNextWord:
            self.pieces.append(text[0].upper())
            self.pieces.append(text[1:])
            self.capitalizeNextWord = 0
        else:
            self.pieces.append(text)

    def parse_Element(self, node):
        """parse an element

        An XML element corresponds to an actual tag in the source:
        <xref id='...'>, <p chance='...'>, <choice>, etc.
        Each element type is handled in its own method.  Like we did in
        parse(), we construct a method name based on the name of the
        element ("do_xref" for an <xref> tag, etc.) and
        call the method.
        """
        handlerMethod = getattr(self, "do_%s" % node.tagName)
        handlerMethod(node)

    def parse_Comment(self, node):
        """parse a comment

        The grammar can contain XML comments, but we ignore them
        """
        pass

    def do_xref(self, node):
        """handle <xref id='...'> tag

        An <xref id='...'> tag is a cross-reference to a <ref id='...'>
        tag.  <xref id='sentence'/> evaluates to a randomly chosen child of
        <ref id='sentence'>.
        """
        id = node.attributes["id"].value
        self.parse(self.randomChildElement(self.refs[id]))

    def do_p(self, node):
        """handle <p> tag

        The <p> tag is the core of the grammar.  It can contain almost
        anything: freeform text, <choice> tags, <xref> tags, even other
        <p> tags.  If a "class='sentence'" attribute is found, a flag
        is set and the next word will be capitalized.  If a "chance='X'"
        attribute is found, there is an X% chance that the tag will be
        evaluated (and therefore a (100-X)% chance that it will be
        completely ignored)
        """
        keys = node.attributes.keys()
        if "class" in keys:
            if node.attributes["class"].value == "sentence":
                self.capitalizeNextWord = 1
        if "chance" in keys:
            chance = int(node.attributes["chance"].value)
            doit = (chance > random.randrange(100))
        else:
            doit = 1
        if doit:
            for child in node.childNodes: self.parse(child)

    def do_choice(self, node):
        """handle <choice> tag

        A <choice> tag contains one or more <p> tags.  One <p> tag
        is chosen at random and evaluated; the rest are ignored.
        """
        self.parse(self.randomChildElement(node))

def usage():
    print __doc__

def main(argv):
    grammar = "kant.xml"
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-d':
            global _debug
            _debug = 1
        elif opt in ("-g", "--grammar"):
            grammar = arg

    source = "".join(args)

    k = KantGenerator(grammar, source)
    #print k.output()



class BaseHTMLProcessor(sgmllib.SGMLParser):
    def reset(self):
        self.pieces = []
        sgmllib.SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):
        stattrs = ''.join([' %s = "%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(stattrs)s>" % locals())

    def unknown_endtag(self, tag):
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):
        self.pieces.append("&%(ref)s" % locals())
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    def handle_data(self, data):
        self.pieces.append(data)

    def handle_comment(self, text):
        self.pieces.append("<!-%(text)s->" % locals())

    def handle_pi(self, data):
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, decl):
        self.pieces.append("<!%(decl)s>" % locals())

    def output(self):
        return "".join(self.pieces)


class Dialectizer(BaseHTMLProcessor):
    subs = ()
    def reset(self):
        self.verbatim = 0
        BaseHTMLProcessor.reset(self)

    def start_pre(self, attrs):
        self.verbatim += 1
        self.unknown_starttag("pre", attrs)

    def end_pre(self):
        self.unknown_endtag("pre")
        self.verbatim -= 1

    def handle_data(self, text):
        self.pieces.append(self.verbatim and text or self.process(text))

    def process(self,text):
        for fromPattern, toPattern in self.subs:
            text = re.sub(fromPattern, toPattern, text)
        return text


class ChefDialectizer(Dialectizer):
    subs = ((r'a([nu])', r'u\1'),
            (r'A([nu])', r'U\1'),
            (r'a\B', r'e'),
            (r'A\B', r'E'),
            (r'en\b', r'ee'),
            (r'\Bew', r'oo'),
            (r'\Be\b', r'e-a'),
            (r'\be', r'i'),
            (r'\bE', r'I'),
            (r'\Bf', r'ff'),
            (r'\Bir', r'ur'),
            (r'(\w*?)i(\w*?)$', r'\1ee\2'),
            (r'\bow', r'oo'),
            (r'\bo', r'oo'),
            (r'\bO', r'Oo'),
            (r'the', r'zee'),
            (r'The', r'Zee'),
            (r'th\b', r't'),
            (r'\Btion', r'shun'),
            (r'\Bu', r'oo'),
            (r'\BU', r'Oo'),
            (r'v', r'f'),
            (r'V', r'F'),
            (r'w', r'w'),
            (r'W', r'W'),
            (r'([a-z])[.]', r'\1.  Bork Bork Bork!'))


def translate(url, dialectName = "chef"):
    import urllib
    sock = urllib.urlopen(url)
    htmlSource = sock.read()
    sock.close()
    parserName = "%sDialectizer" % dialectName.capitalize()
    parserClass = globals()[parserName]
    parser = parserClass()
    parser.feed(htmlSource)
    parser.close()
    return parser.output()

def test(url):
    for dialect in ("chef",):
        outfile = "%s.html" % dialect
        fsock = open(outfile, "wb")
        fsock.write(translate(url, dialect))
        fsock.close()
        import webbrowser
        webbrowser.open_new(outfile)






class SGMLFilter(sgmllib.SGMLParser):
    def __init__(self, outfile = None, infile = None):
        sgmllib.SGMLParser.__init__(self)
        if outfile is None:
            outfile = sys.stdout
        self.write = outfile.write
        if infile is not None:
            self.load(infile)

    def load(self, infile):
        while 1:
            s = infile.read(512)
            if not s:
                break
            self.feed(s)
        self.close()

    def handle_entityref(self, name):
        self.write("&%s;" % name)

    def handle_data(self, data):
        self.write(cgi.escape(data))

    def unknown_starttag(self, tag, attrs):
        tag, attrs = self.start(tag, attrs)
        if tag:
            if not attrs:
                self.write("<%s>" % tag)
            else:
                self.write("<%s" % tag)
                for k, v in attrs:
                    self.write(" %s=%s" % (k,repr(v)))
                self.write(">")

    def unknown_endtag(self, tag):
        tag = self.end(tag)
        if tag:
            self.write("</%s>" % tag)

    def start(self, tag, attrs):
        return tag, attrs

    def end(self, tag):
        return tag


class Filter(SGMLFilter):
    def fixtag(self, tag):
        if tag == "em":
            tag = "i"
        if tag == "string":
            tag = "b"
        return string.upper(tag)

    def start(self, tag, attrs):
        return self.fixtag(tag), attrs

    def end(self, tag):
        return self.fixtag(tag)

def testSgmllib():
    c = Filter()
    f = open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html")
    c.load(f)
    f.close()

class WellFormedChecker(sgmllib.SGMLParser):
    def __init__(self, f=None):
        sgmllib.SGMLParser.__init__(self)
        self.tags = []
        if f:
            self.load(f)

    def load(self, f):
        while 1:
            s = f.read(512)
            if not s:
                break
            self.feed(s)
        self.close()

    def close(self):
        sgmllib.SGMLParser.close(self)
        if self.tags:
            raise SyntaxError, "start tag %s not close" % self.tags[-1]

    def unknown_starttag(self, start, attrs):
        self.tags.append(start)

    def unknown_endtag(self, end):
        start = self.tags.pop()
        if end != start:
            raise SyntaxError, "end tag %s not match start tag %s" % (end, start)


def testcheck():
    try:
        c = WellFormedChecker()
        c.load(open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html"))
    except SyntaxError:
        raise
    else:
        print "done.the document is Well Formed"


class PrettyPrinter(sgmllib.SGMLParser):
    def __init__(self):
        sgmllib.SGMLParser.__init__(self)
        self.flag = 0

    def newline(self):
        if self.flag:
            sys.stdout.write("\n")
        self.flag = 0

    def unknown_starttag(self, tag, attrs):
        text = ""
        for attr, value in attrs:
            text = text + " %s = '%s'" % (attr,cgi.escape(value))
        self.newline()
        sys.stdout.write("<%s%s>\n" % (tag,text))

    def handle_data(self, text):
        sys.stdout.write(text)
        self.flag = (text[-1:] != "\n")

    def handle_entityref(self, text):
        sys.stdout.write("&%s;" % text)

    def unknown_endtag(self, tag):
        self.newline()
        sys.stdout.write("<%s>" % tag)


def testUnkown():
    p = PrettyPrinter()
    f = open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html")
    p.feed(f.read())
    p.close()


class FoundTitle(Exception):
    pass


class ExtractTitle(sgmllib.SGMLParser):
    def __init__(self, verbose=0):
        sgmllib.SGMLParser.__init__(self, verbose)
        self.title = self.data = None

    def handle_data(self, data):
        if self.data is not None:
            self.data.append(data)

    def start_title(self, attrs):
        self.data = []

    def end_title(self):
        self.title = string.join(self.data,"")
        raise FoundTitle


def extract(myFile):
    p = ExtractTitle()
    try:
        while 1:
            s = myFile.read(512)
            if not s:
                break
            p.feed(s)
        p.close()
    except FoundTitle:
        return p.title
    return None


def testSgml():
    print "html", "=>", extract(open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html"))


def testformatter():
    w = formatter.AbstractWriter()
    f = formatter.AbstractFormatter(w)
    myfile = open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html")
    p = htmllib.HTMLParser(f)
    p.feed(myfile.read())
    p.close()
    myfile.close()

def testformatter1():
    w = formatter.DumbWriter(cStringIO.StringIO())
    f = formatter.AbstractFormatter(w)
    myfile = open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html")
    p = htmllib.HTMLParser(f)
    p.feed(myfile.read())
    p.close()
    myfile.close()
    #print "\n****** %s",p.anchorlist

class Parser(htmllib.HTMLParser):
    def __init__(self):
        self.anchors = {}
        f = formatter.NullFormatter()
        htmllib.HTMLParser.__init__(self, f)

    def anchor_bgn(self, href, name, type):
        self.save_bgn()
        self.anchor = href

    def anchor_end(self):
        text = string.strip(self.save_end())
        if self.anchor and text:
            self.anchors[text] = self.anchors.get(text, []) + [self.anchor]


def testHtml():
    myFile = open(r"E:\code\huang\b\zhuoqiang.me\category\programming.html")
    myHtml = myFile.read()
    myFile.close()
    p = Parser()
    p.feed(myHtml)
    p.close()

    for k, v in p.anchors.items():
        print k, "=>", v


class Foo(object):
    def __init__(self, myDict):
        self.data = myDict

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, item):
        self.data[key] = item

    def __repr__(self):
        return repr(self.data)

    def __cmp__(self, foo):
        if isinstance(foo, Foo):
            return cmp(self.data, foo.data)

    def __len__(self): return len(self.data)

    def __delitem__(self, key):
        del self.data[key]

    def __parse(self):
        print len(self.data)


def testFoo():
    myDict = {"a":1,"b":2}
    foo = Foo(myDict)
    foo["c"] = 3
    print foo["a"]
    dict1 = {"b":2}
    foo1 = Foo(dict1)
    print foo1 < foo
    print repr(foo)
    del foo["c"]
    print repr(foo)


def Indent(dom, node, indent=0):
    children = node.childNodes[:]
    if indent:
        text = dom.createTextNode('%%' + '##' * indent)
        node.parentNode.insertBefore(text, node)
    if children:
        if children[-1].nodeType == node.ELEMENT_NODE:
            text = dom.createTextNode('##' + '%%' * indent)
            node.appendChild(text)
        for n in children:
            if n.nodeType == node.ELEMENT_NODE:
                Indent(dom, n, indent + 1)

def testDom():
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, "catalog", None)
    root = dom.documentElement
    item = dom.createElement('item')
    text = dom.createTextNode('123')
    item.appendChild(text)
    item.setAttribute('id','value')
    root.appendChild(item)
    domCopy = dom.cloneNode(True)
    Indent(domCopy, domCopy.documentElement)
    f = open("test.xml", 'w')
    domCopy.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
    domCopy.unlink()
    f.close()



if __name__ == "__main__":
    pass
#    testcheck()
    testSgml()
    testHtml()
    testUnkown()
    testSgmllib()
    testformatter1()
    testFoo()
    test("http://woodpecker.org.cn/diveintopython/native_data_types/lists.html")
#    main(sys.argv[1:])
    testDom()


def testxmldom():
    f = open(r"E:\code\huang\b\py\kgp\husserl.xml")
    xmldom = xml.dom.minidom.parse(f)
    domCopy = xmldom.cloneNode(True)
    Indent(domCopy, domCopy.documentElement)
    fw = open(r"E:\code\huang\b\zhuoqiang.me\category\programmi.xml", 'w')
    domCopy.writexml(fw, encoding='utf-8')
    domCopy.unlink()
    fw.close()
    f.close()
