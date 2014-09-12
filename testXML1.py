Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Foo:
	def __init__(self,x):
		self.x = x
	def bar(self,y):
		self.x += y

		
>>> f = Foo(10)
>>> f
<__main__.Foo object at 0x01F74070>
>>> type(f)
<class '__main__.Foo'>
>>> Foo.__class__
<class 'type'>
>>> Foo.__subclasshook__
<built-in method __subclasshook__ of type object at 0x01F9A8F0>
>>> Foo.__dict__
mappingproxy({'bar': <function Foo.bar at 0x01F9C348>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Foo' objects>, '__init__': <function Foo.__init__ at 0x01F644B0>})
>>> Foo.__mro__
(<class '__main__.Foo'>, <class 'object'>)
>>> import urllib.request
>>> import xml.etree.ElementTree
>>> u = urllib.request.urlopen("http://planet.python.org/rss20.xml")
>>> u
<http.client.HTTPResponse object at 0x02283690>
>>> doc = xml.etree.ElementTree.parse(u)
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x0227B210>
>>> doc.getroot()
<Element 'rss' at 0x022729F0>
>>> root = doc.getroot()
>>> root.tag
'rss'
>>> root.attrib
{'version': '2.0'}
>>> for child_of_root in root:
	print child_of_root.tag
	
SyntaxError: invalid syntax
>>> for child_of_root in root:
	print(child_of_root.tag,end=",")

	
channel,
>>> child_of_root
<Element 'channel' at 0x02272900>
>>> root[0]
<Element 'channel' at 0x02272900>
>>> iter(root)
<iterator object at 0x022836D0>
>>> it = iter(root)
>>> next(it)
<Element 'channel' at 0x02272900>
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    next(it)
StopIteration
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x0227B210>
>>> import lxml
>>> doc1 = lxml.etree.parse(u)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    doc1 = lxml.etree.parse(u)
AttributeError: 'module' object has no attribute 'etree'
>>> import lxml.etree
>>> doc1 = lxml.etree.parse(u)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    doc1 = lxml.etree.parse(u)
  File "lxml.etree.pyx", line 3239, in lxml.etree.parse (src\lxml\lxml.etree.c:69970)
  File "parser.pxi", line 1770, in lxml.etree._parseDocument (src\lxml\lxml.etree.c:102272)
  File "parser.pxi", line 1790, in lxml.etree._parseFilelikeDocument (src\lxml\lxml.etree.c:102531)
  File "parser.pxi", line 1685, in lxml.etree._parseDocFromFilelike (src\lxml\lxml.etree.c:101457)
  File "parser.pxi", line 1134, in lxml.etree._BaseParser._parseDocFromFilelike (src\lxml\lxml.etree.c:97084)
  File "parser.pxi", line 582, in lxml.etree._ParserContext._handleParseResultDoc (src\lxml\lxml.etree.c:91290)
  File "parser.pxi", line 683, in lxml.etree._handleParseResult (src\lxml\lxml.etree.c:92476)
  File "parser.pxi", line 622, in lxml.etree._raiseParseError (src\lxml\lxml.etree.c:91772)
  File "<string>", line None
lxml.etree.XMLSyntaxError: Document is empty, line 1, column 1
>>> u = urllib.request.urlopen("http://planet.python.org/rss20.xml")
>>> doc1 = lxml.etree.parse(u)
>>> doc1
<lxml.etree._ElementTree object at 0x0228D350>
>>> alist = [1,2,3,4,5,6,7,8,9,0]
>>> alist.pop()
0
>>> alist
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> alist.remove(5)
>>> alist
[1, 2, 3, 4, 6, 7, 8, 9]
>>> alist.remove(7)
>>> alist
[1, 2, 3, 4, 6, 8, 9]
>>> alist.pop()
9
>>> alist
[1, 2, 3, 4, 6, 8]
>>> alist.pop()
8
>>> alist
[1, 2, 3, 4, 6]
>>> alist[-2]
4
>>> alist[-2].remove(6)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    alist[-2].remove(6)
AttributeError: 'int' object has no attribute 'remove'
>>> s = ".//a/b"
>>> s.split('/')
['.', '', 'a', 'b']
>>> path.split('[./]')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    path.split('[./]')
NameError: name 'path' is not defined
>>> s.split('[./]')
['.//a/b']
>>> .split('./')
SyntaxError: invalid syntax
>>> s.split('./')
['', '/a/b']
>>> path.split('.|/')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    path.split('.|/')
NameError: name 'path' is not defined
>>> s.split((',','/'))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.split((',','/'))
TypeError: Can't convert 'tuple' object to str implicitly
>>> ' 1  2   3  '.split(' ')
['', '1', '', '2', '', '', '3', '', '']
>>> ' 1  2   3  '.split()
['1', '2', '3']
>>> ".//a/b".split()
['.//a/b']
>>> ".//a/b".split('/')
['.', '', 'a', 'b']
>>> import re
>>> re.match("\w+","ab0")
<_sre.SRE_Match object; span=(0, 3), match='ab0'>
>>> re.match("\w+","ab/")
<_sre.SRE_Match object; span=(0, 2), match='ab'>
>>> re.search("\w+","ab0")
<_sre.SRE_Match object; span=(0, 3), match='ab0'>
>>> re.search("\w+","ab/")
<_sre.SRE_Match object; span=(0, 2), match='ab'>
>>> re.search("\w+","/.ab/")
<_sre.SRE_Match object; span=(2, 4), match='ab'>
>>> re.match("\w+","/ab/")
>>> [1,2,3,4].remove(5)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    [1,2,3,4].remove(5)
ValueError: list.remove(x): x not in list
>>> [1,2,5,5].remove(5)
>>> alist = [1,2,5,5]
>>> alist.remove(5)
>>> alist
[1, 2, 5]
>>> alist
[1, 2, 5]
>>> alist[-6:]
[1, 2, 5]
>>> alist[:9]
[1, 2, 5]
>>> ".//*[@name='Singapore']/year".split('.')
['', "//*[@name='Singapore']/year"]
>>> ".//*[@name='Singapore']/year",split('/')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    ".//*[@name='Singapore']/year",split('/')
NameError: name 'split' is not defined
>>> ".//*[@name='Singapore']/year".split('/')
['.', '', "*[@name='Singapore']", 'year']
>>> def dict_to_xml(tag,d):
	elem = xml.etree.ElementTree.Element(tag)
	for key,val in d.items():
		child = xml.etree.ElementTree.Element(key)
		child.text = str(val)
		elem.append(child)
	return elem

>>> s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
>>> e = dict_to_xml("stock",s)
>>> e
<Element 'stock' at 0x0252A690>
>>> xml.etree.ElementTree.dump(e)
<stock><price>490.1</price><name>GOOG</name><shares>100</shares></stock>
>>> ee = xml.etree.ElementTree.dump(e)
<stock><price>490.1</price><name>GOOG</name><shares>100</shares></stock>
e
>>> e
<Element 'stock' at 0x0252A690>
>>> ee
>>> ee
>>> ee = xml.etree.ElementTree.dump(e)
<stock><price>490.1</price><name>GOOG</name><shares>100</shares></stock>
>>> ee
>>> xml.etree.ElementTree.dump(e)
<stock><price>490.1</price><name>GOOG</name><shares>100</shares></stock>
>>> xml.etree.ElementTree.tostring(e)
b'<stock><price>490.1</price><name>GOOG</name><shares>100</shares></stock>'
>>> x = xml.etree.ElementTree.tostring(e)
>>> x
b'<stock><price>490.1</price><name>GOOG</name><shares>100</shares></stock>'
>>> type(x)
<class 'bytes'>
>>> e.set("_id",1234)
>>> e
<Element 'stock' at 0x0252A690>
>>> xml.etree.ElementTree.tostring(e)
Traceback (most recent call last):
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 1081, in _escape_attrib
    if "&" in text:
TypeError: argument of type 'int' is not iterable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    xml.etree.ElementTree.tostring(e)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 1126, in tostring
    short_empty_elements=short_empty_elements)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 778, in write
    short_empty_elements=short_empty_elements)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 935, in _serialize_xml
    v = _escape_attrib(v)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 1093, in _escape_attrib
    _raise_serialization_error(text)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 1059, in _raise_serialization_error
    "cannot serialize %r (type %s)" % (text, type(text).__name__)
TypeError: cannot serialize 1234 (type int)
>>> e.set("_id","1234")
>>> xml.etree.ElementTree.tostring(e)
b'<stock _id="1234"><price>490.1</price><name>GOOG</name><shares>100</shares></stock>'
>>> OrderedDict
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    OrderedDict
NameError: name 'OrderedDict' is not defined
>>> import collections
>>> collections.OrderedDict
<class 'collections.OrderedDict'>
>>> od = collections.OrderedDict()
>>> od['name'] = 'good'
>>> od
OrderedDict([('name', 'good')])
>>> od['price'] = 
KeyboardInterrupt
s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
>>> od['price'] = 490.1
>>> od['shares'] = 100
>>> od
OrderedDict([('name', 'good'), ('price', 490.1), ('shares', 100)])
>>> oe = dict_to_xml("stock",od)
>>> oe
<Element 'stock' at 0x025496C0>
>>> xml.etree.ElementTree.tostring(oe)
b'<stock><name>good</name><price>490.1</price><shares>100</shares></stock>'
>>> "<{}>".format(10,20)
'<10>'
>>> "<{1}>".format(10,20)
'<20>'
>>> def dict_to_xml_str(tag,d):
	parts = ["<{}>".format(tag)]
	for key,item in d.items():
		parts.append("<{0}>{1}</{0}>".format(key,val))
	parts.append("</{0}>".format(tag))
	return ''.join(parts)

>>> xmlstr = dict_to_xml_str("stock",od)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    xmlstr = dict_to_xml_str("stock",od)
  File "<pyshell#133>", line 4, in dict_to_xml_str
    parts.append("<{0}>{1}</{0}>".format(key,val))
NameError: name 'val' is not defined
>>> def dict_to_xml_str(tag,d):
	parts = ["<{}>".format(tag)]
	for key,item in d.items():
		parts.append("<{0}>{1}</{0}>".format(key,item))
	parts.append("</{0}>".format(tag))
	return ''.join(parts)

>>> xmlstr = dict_to_xml_str("stock",od)
>>> xmlstr
'<stock><name>good</name><price>490.1</price><shares>100</shares></stock>'
>>> d = { 'name' : '<spam>' }
>>> xmlstr = dict_to_xml_str("stock",d)
>>> xmlstr
'<stock><name><spam></name></stock>'
>>> myxml = dict_to_xml("stock",d)
>>> myxml
<Element 'stock' at 0x025497E0>
>>> xml.etree.ElementTree.tostring(myxml)
b'<stock><name>&lt;spam&gt;</name></stock>'
>>> import xml.sax.saxutils
>>> xml.sax.saxutils.escape("<spam>")
'&lt;spam&gt;'
>>> xml.sax.saxutils.unescape(_)
'<spam>'
>>> root = xml.etree.ElementTree.parse("E:/code/huang/b/learnpy/test.xml")
>>> root
<xml.etree.ElementTree.ElementTree object at 0x0252EA90>
>>> cr = root.iterfind("rt")
>>> cr
<generator object select at 0x0255A7D8>
>>> next(cr)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    next(cr)
StopIteration
>>> cr = root.iterfind("cr")
>>> cr
<generator object select at 0x0255A8C8>
>>> next(cr)
<Element 'cr' at 0x025645A0>
>>> next(cr)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    next(cr)
StopIteration
>>> for cr in root.iterfind("cr"):
	root.remove(cr)

	
Traceback (most recent call last):
  File "<pyshell#159>", line 2, in <module>
    root.remove(cr)
AttributeError: 'ElementTree' object has no attribute 'remove'
>>> doc = root
>>> root = doc.getroot()
>>> root
<Element 'stop' at 0x02564330>
>>> cr =root.iterfind("cr")

	
>>> cr
<generator object select at 0x0255ADA0>
>>> next(cr)
<Element 'cr' at 0x025645A0>
>>> for cr in root.iterfind("cr"):
	root.remove(cr)

	
>>> root
<Element 'stop' at 0x02564330>
>>>  cr = root.iterfind("cr")
 
SyntaxError: unexpected indent
>>> cr = root.iterfind("cr")
>>> ce
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    ce
NameError: name 'ce' is not defined
>>> cr
<generator object select at 0x0255AA30>
>>> next(cr)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    next(cr)
StopIteration
>>> root.getchildren()
[<Element 'id' at 0x02564540>, <Element 'nm' at 0x02564450>, <Element 'sri' at 0x02564480>, <Element 'pre' at 0x025645D0>, <Element 'pre' at 0x02564690>]
>>> root.getchildren().index(root.find("nm"))
1
>>> dir(root)
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set']
>>> e = xml.etree.ElementTree.Element('spam')
>>> e
<Element 'spam' at 0x02564390>
>>> e.text = "test test"
>>> root.insert(root.getchildren().index(root.find("nm")),e)
>>> root.getchildren()
[<Element 'id' at 0x02564540>, <Element 'spam' at 0x02564390>, <Element 'nm' at 0x02564450>, <Element 'sri' at 0x02564480>, <Element 'pre' at 0x025645D0>, <Element 'pre' at 0x02564690>]
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x0252EA90>
>>> root
<Element 'stop' at 0x02564330>
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x0252EA90>
>>> doc.write("newtest.xml",xml_declaration=True)
>>> doc.write("newtest.xml",xml_declaration=True)
>>> doc.write("newtest.xml",xml_declaration=False)
>>> doc.write("newtest.xml")
>>> root[0]
<Element 'id' at 0x02564540>
>>> root[1]
<Element 'spam' at 0x02564390>
>>> root.getchildren()
[<Element 'id' at 0x02564540>, <Element 'spam' at 0x02564390>, <Element 'nm' at 0x02564450>, <Element 'sri' at 0x02564480>, <Element 'pre' at 0x025645D0>, <Element 'pre' at 0x02564690>]
>>> doc = xml.etree.ElementTree("E:/code/huang/b/learnpy/test.xml")
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    doc = xml.etree.ElementTree("E:/code/huang/b/learnpy/test.xml")
TypeError: 'module' object is not callable
>>> doc = xml.etree.ElementTree.parse("E:/code/huang/b/learnpy/test.xml")
>>> doc
<xml.etree.ElementTree.ElementTree object at 0x0252EAD0>
>>> root = doc.getroot()
>>> root
<Element 'top' at 0x025645A0>
>>> content = doc.find(".//content")
>>> content
<Element 'content' at 0x025647E0>
>>> html = content.find("html")
>>> html
>>> content = root.find(".//content")
>>> content
<Element 'content' at 0x025647E0>
>>> html = content.find("{http://www.w3.org/1999/xhtml}html")
>>> html
<Element '{http://www.w3.org/1999/xhtml}html' at 0x02564840>
>>> head = content.find("{http://www.w3.org/1999/xhtml}html/head")
>>> head
>>> head = content.find("{http://www.w3.org/1999/xhtml}html/{http://www.w3.org/1999/xhtml}head")
>>> head
<Element '{http://www.w3.org/1999/xhtml}head' at 0x025648A0>
>>> head.text
'\n              '
>>> head.find("{http://www.w3.org/1999/title"}
SyntaxError: invalid syntax
>>> head.find("{http://www.w3.org/1999/title"})
SyntaxError: invalid syntax
>>> head.find("{http://www.w3.org/1999/xhtml}title")
<Element '{http://www.w3.org/1999/xhtml}title' at 0x02564900>
>>> head.find("{http://www.w3.org/1999/xhtml}title").text
'Hello World'
>>> "a = {a},b={b}".format(a=5,b=10)
'a = 5,b=10'
>>> "a = {a},b={b}".format({'a':5,'b':10})
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    "a = {a},b={b}".format({'a':5,'b':10})
KeyError: 'a'
>>> "a= {0['a']},b={0['a']}".format({'a':5,'b':10})
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> "a= {0['a']},b={0['a']}".format({'a':5,'b':10})
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    "a= {0['a']},b={0['a']}".format({'a':5,'b':10})
KeyError: "'a'"
>>> "a= {0.a},b={0.a]}".format({'a':5,'b':10})
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    "a= {0.a},b={0.a]}".format({'a':5,'b':10})
AttributeError: 'dict' object has no attribute 'a'
>>> "{a}".format_map({'a':5,'b':10})
'5'
>>> "a = {a}".format_map({'a':5,'b':10})
'a = 5'
>>> "{a}".format(**{'a':5,'b':10})
'5'
>>> html = "http://www.w3.org/1999/title"
>>> def pathhtml(path):
	path.format(html)

	
>>> head.find("{html}title")
>>> def pathhtml(path):
	return path.format(html)

>>> head.find(pathhtml("{html}title"))
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    head.find(pathhtml("{html}title"))
  File "<pyshell#229>", line 2, in pathhtml
    return path.format(html)
KeyError: 'html'
>>> html
'http://www.w3.org/1999/title'
>>> def pathhtml(path,html):
	namespace={"html":html}
	return path.format(namespace)

>>> def pathhtml(path,html):
	return path.format({"html":html})

>>> import collections
>>> import functiontools
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    import functiontools
ImportError: No module named 'functiontools'
>>> import functionstool
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    import functionstool
ImportError: No module named 'functionstool'
>>> import functools
>>> functools.partial(pathhtml,html)
functools.partial(<function pathhtml at 0x02565618>, 'http://www.w3.org/1999/title')
>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml
functools.partial(<function pathhtml at 0x02565618>, 'http://www.w3.org/1999/title')
>>> dir(partialpathhtml)
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'args', 'func', 'keywords']
>>> partialpathhtml.func
<function pathhtml at 0x02565618>
>>> partialpathhtml("{html}")
'http://www.w3.org/1999/title'
>>> head.find(partialpathhtml("{html}title"))
Traceback (most recent call last):
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 257, in iterfind
    selector = _cache[cache_key]
KeyError: ('http://www.w3.org/1999/title', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 80, in xpath_tokenizer
    raise KeyError
KeyError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    head.find(partialpathhtml("{html}title"))
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 290, in find
    return next(iterfind(elem, path, namespaces))
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 264, in iterfind
    token = next()
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 83, in xpath_tokenizer
    raise SyntaxError("prefix %r not found in prefix map" % prefix)
  File "<string>", line None
SyntaxError: prefix 'http' not found in prefix map
>>> partialpathhtml("{html}title")
'http://www.w3.org/1999/title'
>>> def pathhtml(path,html):
	namespace["html"]='{'+ html + '}'
	return path.format(namespace)

>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml
functools.partial(<function pathhtml at 0x02565F60>, 'http://www.w3.org/1999/title')
>>> partialpathhtml("{html}")
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    partialpathhtml("{html}")
  File "<pyshell#250>", line 2, in pathhtml
    namespace["html"]='{'+ html + '}'
NameError: name 'namespace' is not defined
>>> def pathhtml(path,html):
	namespace = {}
	namespace["html"]='{'+ html + '}'
	return path.format(namespace)

>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml("{html}")
'http://www.w3.org/1999/title'
>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml
functools.partial(<function pathhtml at 0x02565F18>, 'http://www.w3.org/1999/title')
>>> partialpathhtml("{html}")
'http://www.w3.org/1999/title'
>>> def pathhtml(path,html):
	namespace = {}
	namespace["html"]='{'+ html + '}'
	return path.format(namespace)

>>> partialpathhtml = functools.partial(pathhtml,html)
>>> 
>>> def pathhtml(path,html):
	namespace = {}
	namespace["html"]='{'+ html + '}'
	return path.format(**namespace)

>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml("{html}")
'http://www.w3.org/1999/title'
>>> pathhtml("{html}",html)
'{http://www.w3.org/1999/title}'
>>> def pathhtml(html,path):
	namespace = {}
	namespace["html"]='{'+ html + '}'
	return path.format(**namespace)

>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml("{html}")
'{http://www.w3.org/1999/title}'
>>> head.find(partialpathhtml("{html}title"))
>>> x = head.find(partialpathhtml("{html}title"))
>>> x
>>> head
<Element '{http://www.w3.org/1999/xhtml}head' at 0x025648A0>
>>> partialpathhtml("{html}title")
'{http://www.w3.org/1999/title}title'
>>> html
'http://www.w3.org/1999/title'
>>> html = 'http://www.w3.org/1999/xhtml'
>>> partialpathhtml = functools.partial(pathhtml,html)
>>> partialpathhtml("{html}title")
'{http://www.w3.org/1999/xhtml}title'
>>> head.find(partialpathhtml("{html}title"))
<Element '{http://www.w3.org/1999/xhtml}title' at 0x02564900>
>>> for event,elem in xml.etree.ElementTree.iterparse("E:/code/huang/b/learnpy/test.xml",("end","end-ns"))
SyntaxError: invalid syntax
>>> for event,elem in xml.etree.ElementTree.iterparse("E:/code/huang/b/learnpy/test.xml",("end","end-ns")):
	print(event,elem)

	
end <Element 'author' at 0x0256C150>
end <Element '{http://www.w3.org/1999/xhtml}title' at 0x0256C360>
end <Element '{http://www.w3.org/1999/xhtml}head' at 0x0256C300>
end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x0256C3F0>
end <Element '{http://www.w3.org/1999/xhtml}body' at 0x0256C390>
end <Element '{http://www.w3.org/1999/xhtml}html' at 0x0256C2A0>
end-ns None
end <Element 'content' at 0x0256C240>
end <Element 'top' at 0x0256C1B0>
>>> for event,elem in xml.etree.ElementTree.iterparse("E:/code/huang/b/learnpy/test.xml",("end","start-ns","end-ns")):
	print(event,elem)

	
end <Element 'author' at 0x0256C270>
start-ns ('', 'http://www.w3.org/1999/xhtml')
end <Element '{http://www.w3.org/1999/xhtml}title' at 0x0256C4E0>
end <Element '{http://www.w3.org/1999/xhtml}head' at 0x0256C480>
end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x0256C570>
end <Element '{http://www.w3.org/1999/xhtml}body' at 0x0256C510>
end <Element '{http://www.w3.org/1999/xhtml}html' at 0x0256C420>
end-ns None
end <Element 'content' at 0x0256C1E0>
end <Element 'top' at 0x0256C330>
>>> elem
<Element 'top' at 0x0256C330>
>>> lxml
<module 'lxml' from 'E:\\Python34\\lib\\site-packages\\lxml\\__init__.py'>
>>> lxml.etree
<module 'lxml.etree' from 'E:\\Python34\\lib\\site-packages\\lxml\\etree.pyd'>
>>> import lxml.etree
>>> root = lxml.etree.Element('root')
>>> root
<Element root at 0x2566eb8>
>>> lxml.etree.tostring(root)
b'<root/>'
>>> root.tag
'root'
>>> root.append(lxml.etree.Element("child"))
>>> root
<Element root at 0x2566eb8>
>>> root[0]
<Element child at 0x2566d78>
>>> root[1]
Traceback (most recent call last):
  File "<pyshell#302>", line 1, in <module>
    root[1]
  File "lxml.etree.pyx", line 1100, in lxml.etree._Element.__getitem__ (src\lxml\lxml.etree.c:46360)
IndexError: list index out of range
>>> lxml.etree.SubElement(root,"child2")
<Element child2 at 0x2571120>
>>> root[1]
<Element child2 at 0x2571120>
>>> root[0]
<Element child at 0x2566d78>
>>> root.append(lxml.etree.Element("child3"))
>>> lxml.etree.SubElement(root,"child4")
<Element child4 at 0x2571198>
>>> lxml.etree.tostring(root,pretty_print=True)
b'<root>\n  <child/>\n  <child2/>\n  <child3/>\n  <child4/>\n</root>\n'
>>> print(lxml.etree.tostring(root,pretty_print=True))
b'<root>\n  <child/>\n  <child2/>\n  <child3/>\n  <child4/>\n</root>\n'
>>> str(lxml.etree.tostring(root,pretty_print=True))
"b'<root>\\n  <child/>\\n  <child2/>\\n  <child3/>\\n  <child4/>\\n</root>\\n'"
>>> lxml.etree.tostring(root)
b'<root><child/><child2/><child3/><child4/></root>'
>>> root1 = xml.etree.ElementTree.Element("root1")
>>> root1
<Element 'root1' at 0x0256C540>
>>> root1.append(xml.etree.ElementTree.Element("child"))
>>> xml.etree.ElementTree.tostring(root1)
b'<root1><child /></root1>'
>>> z = lxml.etree.tostring(root,pretty_print=True)
>>> dir(z)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> z.decode()
'<root>\n  <child/>\n  <child2/>\n  <child3/>\n  <child4/>\n</root>\n'
>>> print(z.decode())
<root>
  <child/>
  <child2/>
  <child3/>
  <child4/>
</root>

>>> print(lxml.etree.tostring(root,pretty_print=True).decode())
<root>
  <child/>
  <child2/>
  <child3/>
  <child4/>
</root>

>>> print(xml.etree.ElementTree.tostring(root1).decode())
<root1><child /></root1>
>>> import pprint
>>> pprint.pprint(xml.etree.ElementTree.tostring(root1).decode())
'<root1><child /></root1>'
>>> z = b"hello world"
>>> y = "hello world"
>>> y.encode("utf-8")
b'hello world'
>>> y.encode("utf-8") == z
True
>>> z.decode("utf-8") == y
True
>>> types(y,encoding="utf-8")
Traceback (most recent call last):
  File "<pyshell#329>", line 1, in <module>
    types(y,encoding="utf-8")
NameError: name 'types' is not defined
>>> type(z)
<class 'bytes'>
>>> import bytes
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    import bytes
ImportError: No module named 'bytes'
>>> bytes(y,encoding="utf-8")
b'hello world'
>>> print(lxml.etree.tostring(root, pretty_print=True).encoding("utf-8"))
Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    print(lxml.etree.tostring(root, pretty_print=True).encoding("utf-8"))
AttributeError: 'bytes' object has no attribute 'encoding'
>>> print(lxml.etree.tostring(root, pretty_print=True).decoding("utf-8"))
Traceback (most recent call last):
  File "<pyshell#334>", line 1, in <module>
    print(lxml.etree.tostring(root, pretty_print=True).decoding("utf-8"))
AttributeError: 'bytes' object has no attribute 'decoding'
>>> print(lxml.etree.tostring(root, pretty_print=True).encode("utf-8"))
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    print(lxml.etree.tostring(root, pretty_print=True).encode("utf-8"))
AttributeError: 'bytes' object has no attribute 'encode'
>>> print(lxml.etree.tostring(root, pretty_print=True).decode("utf-8"))
<root>
  <child/>
  <child2/>
  <child3/>
  <child4/>
</root>

>>> child = root[0]
>>> child
<Element child at 0x24f07d8>
>>> print(child.tag)
child
>>> print(child.text)
None
>>> len(root)
4
>>> len(root1)
1
>>> root.index(root[2])
2
>>> root.getchildren()
[<Element child at 0x24f07d8>, <Element child2 at 0x25668c8>, <Element child3 at 0x2566440>, <Element child4 at 0x2566648>]
>>> [1,2,3,4,5].index(4,[1,4])
Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    [1,2,3,4,5].index(4,[1,4])
TypeError: slice indices must be integers or None or have an __index__ method
>>> [1,2,3,4,5].index(4)
3
>>> [1,2,3,4,5].index(4,[1,])
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    [1,2,3,4,5].index(4,[1,])
TypeError: slice indices must be integers or None or have an __index__ method
>>> [1,2,3,4,5].index(4,1,])
SyntaxError: invalid syntax
>>> [1,2,3,4,5].index(4,1)
3
>>> [1,2,3,4,5].index(4,3)
3
>>> [1,2,3,4,5].index(4,4])
SyntaxError: invalid syntax
>>> [1,2,3,4,5].index(4,4)
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    [1,2,3,4,5].index(4,4)
ValueError: 4 is not in list
>>> [1,2,3,4,5].index(4,2)
3
>>> [1,2,3,4,5].index(4,1,2)
Traceback (most recent call last):
  File "<pyshell#354>", line 1, in <module>
    [1,2,3,4,5].index(4,1,2)
ValueError: 4 is not in list
>>> [1,2,3,4,5].index(4,1,4)
3
>>> root.index(root[2])
2
>>> root.index(root[2],0)
2
>>> root.index(root[2],0,1)
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    root.index(root[2],0,1)
  File "lxml.etree.pyx", line 1223, in lxml.etree._Element.index (src\lxml\lxml.etree.c:47656)
ValueError: list.index(x): x not in slice
>>> list(root)
[<Element child at 0x24f07d8>, <Element child2 at 0x2566120>, <Element child3 at 0x25661c0>, <Element child4 at 0x25445a8>]
>>> child
<Element child at 0x24f07d8>
>>> child.append(lxml.etree.Element("grand"))
>>> list(root)
[<Element child at 0x24f07d8>, <Element child2 at 0x25663f0>, <Element child3 at 0x2566e18>, <Element child4 at 0x25445a8>]
>>> list(child)
[<Element grand at 0x2544850>]
>>> list(root1)
[<Element 'child' at 0x0256C3C0>]
>>> child.insert(1,lxml.etree.Element("grand1"))
>>> child
<Element child at 0x24f07d8>
>>> child.getchildren()
[<Element grand at 0x25661c0>, <Element grand1 at 0x25663f0>]
>>> start = root[:1]
>>> start
[<Element child at 0x24f07d8>]
>>> root is True
False
>>> if root:
	print(True)

	

Warning (from warnings module):
  File "__main__", line 1
FutureWarning: The behavior of this method will change in future versions. Use specific 'len(elem)' or 'elem is not None' test instead.
True
>>> len(root)
4
>>> if len(root) > 0:
	print(True)

	
True
>>> lxml.etree.iselement(root)
True
>>> xml.etree.ElementTree.iselement(root1)
True
>>> root1
<Element 'root1' at 0x0256C540>
>>> root
<Element root at 0x2566eb8>
>>> type(root1)
<class 'xml.etree.ElementTree.Element'>
>>> type(root)
<class 'lxml.etree._Element'>
>>> root
<Element root at 0x2566eb8>
>>> root.getchildren()
[<Element child at 0x24f07d8>, <Element child2 at 0x25663f0>, <Element child3 at 0x25663c8>, <Element child4 at 0x25662b0>]
>>> root[0] = root[-1]
>>> root.getchildren()
[<Element child4 at 0x25662b0>, <Element child2 at 0x25663f0>, <Element child3 at 0x25663c8>]
>>> root1
<Element 'root1' at 0x0256C540>
>>> list(root1)
[<Element 'child' at 0x0256C3C0>]
>>> xml.etree.ElementTree.SubElement(root1,xml.etree.ElementTree.Element("child2"))
<Element <Element 'child2' at 0x02564630> at 0x02564360>
>>> list(root1)
[<Element 'child' at 0x0256C3C0>, <Element <Element 'child2' at 0x02564630> at 0x02564360>]
>>> xml.etree.ElementTree.SubElement(root1,"child3")
<Element 'child3' at 0x0256C450>
>>> xml.etree.ElementTree.tostring(root1)
Traceback (most recent call last):
  File "<pyshell#393>", line 1, in <module>
    xml.etree.ElementTree.tostring(root1)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 1126, in tostring
    short_empty_elements=short_empty_elements)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 775, in write
    qnames, namespaces = _namespaces(self._root, default_namespace)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 887, in _namespaces
    _raise_serialization_error(tag)
  File "E:\Python34\lib\xml\etree\ElementTree.py", line 1059, in _raise_serialization_error
    "cannot serialize %r (type %s)" % (text, type(text).__name__)
TypeError: cannot serialize <Element 'child2' at 0x02564630> (type Element)
>>> root1.remove(1)
Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    root1.remove(1)
TypeError: must be xml.etree.ElementTree.Element, not int
>>> root1.remove(root1[1])
>>> root1.getchildren()
[<Element 'child' at 0x0256C3C0>, <Element 'child3' at 0x0256C450>]
>>> root1.insert(1,xml.etree.ElementTree.Element("child2"))
>>> root1.getchildren()
[<Element 'child' at 0x0256C3C0>, <Element 'child2' at 0x0256C990>, <Element 'child3' at 0x0256C450>]
>>> root1
<Element 'root1' at 0x0256C540>
>>> root1[0] = root1[-1]
>>> root1.getchildren()
[<Element 'child3' at 0x0256C450>, <Element 'child2' at 0x0256C990>, <Element 'child3' at 0x0256C450>]
>>> xml.etree.ElementTree.tostring(root1)
b'<root1><child3 /><child2 /><child3 /></root1>'
>>> dir(root1)
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set']
>>> root1[1].clear()
>>> root1
<Element 'root1' at 0x0256C540>
>>> list(root1)
[<Element 'child3' at 0x0256C450>, <Element 'child2' at 0x0256C990>, <Element 'child3' at 0x0256C450>]
>>> root1.pop()
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    root1.pop()
AttributeError: 'xml.etree.ElementTree.Element' object has no attribute 'pop'
>>> root1.remove(root1[0])
>>> list(root1)
[<Element 'child2' at 0x0256C990>, <Element 'child3' at 0x0256C450>]
>>> root1[0] = root1[1]
>>> list(root1)
[<Element 'child3' at 0x0256C450>, <Element 'child3' at 0x0256C450>]
>>> root1[0].append(xml.etree.ElementTree.Element("grand"))
>>> list(root1)
[<Element 'child3' at 0x0256C450>, <Element 'child3' at 0x0256C450>]
>>> xml.etree.ElementTree.tostring(root1)
b'<root1><child3><grand /></child3><child3><grand /></child3></root1>'
>>> root
<Element root at 0x2566eb8>
>>> len(root)
3
>>> l = [0,1,2,[0,1,2]]
>>> l[0] = l[-1]
>>> l
[[0, 1, 2], 1, 2, [0, 1, 2]]
>>> l[0] is l[-1]
True
>>> root[0].getparent()
<Element root at 0x2566eb8>
>>> root
<Element root at 0x2566eb8>
>>> import copy
>>> list(root1)
[<Element 'child3' at 0x0256C450>, <Element 'child3' at 0x0256C450>]
>>> list(root1[0])
[<Element 'grand' at 0x0256CAE0>]
>>> list(root[0])
[]
>>> list(root)
[<Element child4 at 0x25660a8>, <Element child2 at 0x25663f0>, <Element child3 at 0x2566288>]
>>> list(root[1])
[]
>>> root[0].append(lxml.etree.Element("grand"))
>>> root[0][0]
<Element grand at 0x25662b0>
>>> root.append(copy.deepcopy(root[0]))
>>> list(root)
[<Element child4 at 0x25665a8>, <Element child2 at 0x2566288>, <Element child3 at 0x2571be8>, <Element child4 at 0x25710f8>]
>>> list(root[0])
[<Element grand at 0x2571d00>]
>>> list(root[-1])
[<Element grand at 0x2571be8>]
>>> lxml.etree.tostring(root)
b'<root><child4><grand/></child4><child2/><child3/><child4><grand/></child4></root>'
>>> [c.tag for c in root]
['child4', 'child2', 'child3', 'child4']
>>> root[0].getprevious()
>>> root[1].getprevious()
<Element child4 at 0x25665a8>
>>> root[1].getnext()
<Element child3 at 0x255ae18>
>>> grand1 = lxml.etree.Element("grand1",abc="abc")
>>> grand1
<Element grand1 at 0x25663f0>
>>> lxml.etree.tostring(grand1)
b'<grand1 abc="abc"/>'
>>> grand1 = xml.etree.ElementTree.Element("grand1",abc="abc")
>>> grand1
<Element 'grand1' at 0x0256CA50>
>>> xml.etree.ElementTree.tostring(grand1)
b'<grand1 abc="abc" />'
>>> grand1.get("abc")
'abc'
>>> grand1 = lxml.etree.Element("grand1",abc="abc")
\
>>> grand1
<Element grand1 at 0x25663f0>
>>> grand1.get("a",10)
10
>>> grand1.get("a")
>>> print(grand1.get("a"))
None
>>> grand1.set("hello","huang")
>>> lxml.etree.eostring(grand1)
Traceback (most recent call last):
  File "<pyshell#453>", line 1, in <module>
    lxml.etree.eostring(grand1)
AttributeError: 'module' object has no attribute 'eostring'
>>> lxml.etree.tostring(grand1)
b'<grand1 abc="abc" hello="huang"/>'
>>> grand1.keys()
['abc', 'hello']
>>> grand1.items()
[('abc', 'abc'), ('hello', 'huang')]
>>> grand1.attrib
{'abc': 'abc', 'hello': 'huang'}
>>> dir(grand1)
['__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '_init', 'addnext', 'addprevious', 'append', 'attrib', 'base', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'getnext', 'getparent', 'getprevious', 'getroottree', 'index', 'insert', 'items', 'iter', 'iterancestors', 'iterchildren', 'iterdescendants', 'iterfind', 'itersiblings', 'itertext', 'keys', 'makeelement', 'nsmap', 'prefix', 'remove', 'replace', 'set', 'sourceline', 'tag', 'tail', 'text', 'values', 'xpath']
>>> grand1["hello"]
Traceback (most recent call last):
  File "<pyshell#459>", line 1, in <module>
    grand1["hello"]
  File "lxml.etree.pyx", line 1098, in lxml.etree._Element.__getitem__ (src\lxml\lxml.etree.c:46339)
TypeError: 'str' object cannot be interpreted as an integer
>>> grand1.text
>>> html = lxml.etree.Element("html")
>>> html
<Element html at 0x255afd0>
>>> body = lxml.etree.SubElement(html,"body")
>>> body.text = "TEXT"
>>> br = lxml.etree.SubElement(body,"br")
>>> br
<Element br at 0x2571d28>
>>> br.tail="TAIL"
>>> lxml.etree.tostring(html)
b'<html><body>TEXT<br/>TAIL</body></html>'
>>> html1 = xml.etree.ElementTree.Element("html")
>>> body1 = xml.etree.ElementTree.SubElement(html,"body")
Traceback (most recent call last):
  File "<pyshell#470>", line 1, in <module>
    body1 = xml.etree.ElementTree.SubElement(html,"body")
TypeError: must be xml.etree.ElementTree.Element, not lxml.etree._Element
>>> body1 = xml.etree.ElementTree.SubElement(html1,"body")
>>> body1
<Element 'body' at 0x0256CBA0>
>>> body1.text = "122"
>>> br1 = xml.etree.ElementTree.SubElement(body1,"br")
>>> br1.text = "123"
>>> br1.tail = "1234"
>>> xml.etree.ElementTree.tostring(html1)
b'<html><body>122<br>123</br>1234</body></html>'
>>> lxml.etree.tostring(br)
b'<br/>TAIL'
>>> from xml.etree.ElementTree import ET
Traceback (most recent call last):
  File "<pyshell#479>", line 1, in <module>
    from xml.etree.ElementTree import ET
ImportError: cannot import name 'ET'
>>> import xml.etree.ElementTree as ET
>>> ET.tostring(br1)
b'<br>123</br>1234'
>>> lxml.etree.tostring(br,with_tail=False)
b'<br/>'
>>> lxml.etree.tostring(br,method="text")
b'TAIL'
>>> ET.tostring(br1,method="text")
b'1231234'
>>> ET.tostring(body1,method="text")
b'1221231234'
>>> html.xpath
<built-in method xpath of lxml.etree._Element object at 0x0255AFD0>
>>> html.xpath("string()")
'TEXTTAIL'
>>> lxml.etree.tostring(html)
b'<html><body>TEXT<br/>TAIL</body></html>'
>>> html.xpath("//text()")
['TEXT', 'TAIL']
>>> foo = lxml.etree.XPath("//text()")
>>> print(foo(html))
['TEXT', 'TAIL']
>>> texts=foo(html)
>>> texts[0]
'TEXT'
>>> type(texts[0])
<class 'lxml.etree._ElementUnicodeResult'>
>>> type(texts[1])
<class 'lxml.etree._ElementUnicodeResult'>
>>> texts[0].getparent()
<Element body at 0x252dc60>
>>> texts[1].getparent()
<Element br at 0x2571d28>
>>> x = html.xpath("string()")
>>> type(x)
<class 'lxml.etree._ElementUnicodeResult'>
>>> x.getparent()
>>> texts[0].__dict__
Traceback (most recent call last):
  File "<pyshell#501>", line 1, in <module>
    texts[0].__dict__
AttributeError: 'lxml.etree._ElementUnicodeResult' object has no attribute '__dict__'
>>> dir(texts[0])
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'attrname', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'getparent', 'index', 'is_attribute', 'is_tail', 'is_text', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> texts[0].is_tail
False
>>> texts[0].is_text
True
>>> root
<Element root at 0x2566eb8>
>>> lxml.etree.tostring(root)
b'<root><child4><grand/></child4><child2/><child3/><child4><grand/></child4></root>'
>>> root[0].text = child0
Traceback (most recent call last):
  File "<pyshell#507>", line 1, in <module>
    root[0].text = child0
NameError: name 'child0' is not defined
>>> root[0].text = "child0"
>>> root[1].text = "child1"
>>> root[2].text = "child2"
>>> print(lxml.etree.tostring(root,pretty_print=True).decode("utf=8"))
<root>
  <child4>child0<grand/></child4>
  <child2>child1</child2>
  <child3>child2</child3>
  <child4>
    <grand/>
  </child4>
</root>

>>> root[0][0]
<Element grand at 0x2571f80>
>>> root[0][0].text = grand
Traceback (most recent call last):
  File "<pyshell#513>", line 1, in <module>
    root[0][0].text = grand
NameError: name 'grand' is not defined
>>> root[0][0].text = "grand"
>>> print(lxml.etree.tostring(root,pretty_print=True).decode("utf=8"))
<root>
  <child4>child0<grand>grand</grand></child4>
  <child2>child1</child2>
  <child3>child2</child3>
  <child4>
    <grand/>
  </child4>
</root>

>>> for element in root.iter():
	print("{0} - {1}".format(element.tag,element.text))

	
root - None
child4 - child0
grand - grand
child2 - child1
child3 - child2
child4 - None
grand - None
>>> for element in root.iter(child4):
	print("{0} - {1}".format(element.tag,element.text))

	
Traceback (most recent call last):
  File "<pyshell#521>", line 1, in <module>
    for element in root.iter(child4):
NameError: name 'child4' is not defined
>>> for element in root.iter("child4"):
	print("{0} - {1}".format(element.tag,element.text))

	
child4 - child0
child4 - None
>>> for element in root.iter("child4","child2"):
	print("{0} - {1}".format(element.tag,element.text))

	
child4 - child0
child2 - child1
child4 - None
>>> for element in root.iter("child4","child2"."child"):
	print("{0} - {1}".format(element.tag,element.text))
	
SyntaxError: invalid syntax
>>> 
>>> for element in root.iter("child4","child2","child"):
	print("{0} - {1}".format(element.tag,element.text))

	
child4 - child0
child2 - child1
child4 - None
>>> root.append(lxml.etree.Entity("#234"))
>>> root.append(lxml.etree.Comment("some comment"))
>>> print(lxml.etree.tostring(root,pretty_print=True).decode("utf=8"))
<root><child4>child0<grand>grand</grand></child4><child2>child1</child2><child3>child2</child3><child4><grand/></child4>&#234;<!--some comment--></root>

>>> print(lxml.etree.tostring(root,pretty_print=True).decode("utf=8"))
<root><child4>child0<grand>grand</grand></child4><child2>child1</child2><child3>child2</child3><child4><grand/></child4>&#234;<!--some comment--></root>

>>> print(lxml.etree.tostring(root).decode("utf=8"))
<root><child4>child0<grand>grand</grand></child4><child2>child1</child2><child3>child2</child3><child4><grand/></child4>&#234;<!--some comment--></root>
>>> f = root.iterfind("//child4")
Traceback (most recent call last):
  File "<pyshell#535>", line 1, in <module>
    f = root.iterfind("//child4")
  File "lxml.etree.pyx", line 1498, in lxml.etree._Element.iterfind (src\lxml\lxml.etree.c:50514)
  File "E:\Python34\lib\site-packages\lxml\_elementpath.py", line 271, in iterfind
    selector = _build_path_iterator(path, namespaces)
f  File "E:\Python34\lib\site-packages\lxml\_elementpath.py", line 241, in _build_path_iterator
    raise SyntaxError("cannot use absolute path on element")
  File "<string>", line None
SyntaxError: cannot use absolute path on element
>>> f = root.iterfind("/child4")
Traceback (most recent call last):
  File "<pyshell#536>", line 1, in <module>
    f = root.iterfind("/child4")
  File "lxml.etree.pyx", line 1498, in lxml.etree._Element.iterfind (src\lxml\lxml.etree.c:50514)
  File "E:\Python34\lib\site-packages\lxml\_elementpath.py", line 271, in iterfind
    selector = _build_path_iterator(path, namespaces)
  File "E:\Python34\lib\site-packages\lxml\_elementpath.py", line 241, in _build_path_iterator
    raise SyntaxError("cannot use absolute path on element")
  File "<string>", line None
SyntaxError: cannot use absolute path on element
>>> f = root.iterfind("child4")
>>> f
<generator object select at 0x02579080>
>>> y = next(f)
>>> y
<Element child4 at 0x2579418>
>>> y = next(f)
>>> y
<Element child4 at 0x2579300>
>>> y
<Element child4 at 0x2579300>
>>> y.text
>>> y.tail
>>> y.getnext()
&#234;
>>> root1
<Element 'root1' at 0x0256C540>
>>> list(root1)
[<Element 'child3' at 0x0256C450>, <Element 'child3' at 0x0256C450>]
>>> f = root1.iterfind("//child4")
Traceback (most recent call last):
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 257, in iterfind
    selector = _cache[cache_key]
KeyError: ('//child4', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#549>", line 1, in <module>
    f = root1.iterfind("//child4")
  File "E:\Python34\lib\xml\etree\ElementPath.py", line 262, in iterfind
    raise SyntaxError("cannot use absolute path on element")
  File "<string>", line None
SyntaxError: cannot use absolute path on element
>>> f = root1.iterfind("child4")
>>> f = root1.iterfind(".//child4")
>>> for element in root.iter():
	if isinstance(element.tag,str):
		print("%s - %s" % (element.tag, element.text))
	else:
		print("SPECIAL: %s - %s" % (element, element.text))

		
root - None
child4 - child0
grand - grand
child2 - child1
child3 - child2
child4 - None
grand - None
SPECIAL: &#234; - &#234;
SPECIAL: <!--some comment--> - some comment
>>> f = root1.iterfind("child4")
>>> f
<generator object select at 0x02579080>
>>> g = next(f)
Traceback (most recent call last):
  File "<pyshell#560>", line 1, in <module>
    g = next(f)
StopIteration
>>> f = root1.iterfind(".//child4")
>>> g = next(f)
Traceback (most recent call last):
  File "<pyshell#562>", line 1, in <module>
    g = next(f)
StopIteration
>>> list(root1)
[<Element 'child3' at 0x0256C450>, <Element 'child3' at 0x0256C450>]
>>> f = root1.iterfind("child3")
>>> g = next(f)
>>> g
<Element 'child3' at 0x0256C450>
>>> g.append(ET.Comment("some comment"))
>>> g
<Element 'child3' at 0x0256C450>
>>> list(g)
[<Element 'grand' at 0x0256CAE0>, <Element <function Comment at 0x0227F108> at 0x0257B660>]
>>> for element in root1.iter():
	if isinstance(element.tag,str):
		print("%s - %s" % (element.tag, element.text))
	else:
		print("SPECIAL: %s - %s" % (element, element.text))

		
root1 - None
child3 - None
grand - None
SPECIAL: <Element <function Comment at 0x0227F108> at 0x0257B660> - some comment
child3 - None
grand - None
SPECIAL: <Element <function Comment at 0x0227F108> at 0x0257B660> - some comment
>>> g[0]
<Element 'grand' at 0x0256CAE0>
>>> g[1]
<Element <function Comment at 0x0227F108> at 0x0257B660>
>>> g[1].items()
[]
>>> g.append(ET.ProcessingInstruction("abc"))
>>> g
<Element 'child3' at 0x0256C450>
>>> list(g)
[<Element 'grand' at 0x0256CAE0>, <Element <function Comment at 0x0227F108> at 0x0257B660>, <Element <function ProcessingInstruction at 0x0227F150> at 0x0257B6C0>]
>>> ET.tostring(g)
b'<child3><grand /><!--some comment--><?abc?></child3>'
>>> for element in root1.iter():
	if isinstance(element.tag,str):
		print("%s - %s" % (element.tag, element.text))
	else:
		print("SPECIAL: %s - %s" % (element, element.text))

		
root1 - None
child3 - None
grand - None
SPECIAL: <Element <function Comment at 0x0227F108> at 0x0257B660> - some comment
SPECIAL: <Element <function ProcessingInstruction at 0x0227F150> at 0x0257B6C0> - abc
child3 - None
grand - None
SPECIAL: <Element <function Comment at 0x0227F108> at 0x0257B660> - some comment
SPECIAL: <Element <function ProcessingInstruction at 0x0227F150> at 0x0257B6C0> - abc
>>> g[2]
<Element <function ProcessingInstruction at 0x0227F150> at 0x0257B6C0>
>>> g[2].tag
<function ProcessingInstruction at 0x0227F150>
>>> g[1].tag
<function Comment at 0x0227F108>
>>> g[0]
<Element 'grand' at 0x0256CAE0>
>>> g[1].tag()
<Element <function Comment at 0x0227F108> at 0x0256CD80>
>>> root.append(lxml.etree.ProcessingInstruction("now"))
>>> print(lxml.etree.tostring(root,pretty_print=True).decode("utf=8"))
<root><child4>child0<grand>grand</grand></child4><child2>child1</child2><child3>child2</child3><child4><grand/></child4>&#234;<!--some comment--><?now ?></root>

>>> for element in root.iter():
	if isinstance(element.tag,str):
		print("%s - %s" % (element.tag, element.text))
	else:
		print("SPECIAL: %s - %s" % (element, element.text))

		
root - None
child4 - child0
grand - grand
child2 - child1
child3 - child2
child4 - None
grand - None
SPECIAL: &#234; - &#234;
SPECIAL: <!--some comment--> - some comment
SPECIAL: <?now?> - 
>>> element
<?now?>
>>> type(element)
<class 'lxml.etree._ProcessingInstruction'>
>>> for element in root.iter(tag="child4"):
	print("%s - %s" % (element.tag, element.text))

	
child4 - child0
child4 - None
>>> for element in root.iter(etree.Element):
	print("%s - %s" % (element.tag, element.text))

	
Traceback (most recent call last):
  File "<pyshell#596>", line 1, in <module>
    for element in root.iter(etree.Element):
NameError: name 'etree' is not defined
>>> for element in root.iter(lxml.etree.Element):
	print("%s - %s" % (element.tag, element.text))

	
root - None
child4 - child0
grand - grand
child2 - child1
child3 - child2
child4 - None
grand - None
>>> for element in root.iter(lxml.etree.Entity
			 ):
	print("%s" % element.text)

	
&#234;
>>> for element in root.iter('*'):
	print("%s" % element.text)

	
None
child0
grand
child1
child2
None
None
>>> for element in root.iter('.'):
	print("%s - %s" % (element.tag, element.text))

	
>>> for element in root.iter('*'):
	print("%s - %s" % (element.tag, element.text))

	
root - None
child4 - child0
grand - grand
child2 - child1
child3 - child2
child4 - None
grand - None
>>> abc = lxml.etree.XML("<root><a><b/></a></root>")
>>> abc
<Element root at 0x2579f30>
>>> lxml.etree.tostring(abc)
b'<root><a><b/></a></root>'
>>> abc1 = ET.XML("<root><a><b/></a></root>")
>>> ET.tostring(abc1)
b'<root><a><b /></a></root>'
>>> lxml.etree.tostring(abc, xml_declaration=True))
SyntaxError: invalid syntax
>>> lxml.etree.tostring(abc, xml_declaration=True)
b"<?xml version='1.0' encoding='ASCII'?>\n<root><a><b/></a></root>"
>>> test = lxml.etree.XML('<html><head/><body><p>Hello<br/>World</p></body></html>')
>>> lxml.etree.tostring(test)
b'<html><head/><body><p>Hello<br/>World</p></body></html>'
>>> lxml.etree.tostring(test,method="test")
Traceback (most recent call last):
  File "<pyshell#616>", line 1, in <module>
    lxml.etree.tostring(test,method="test")
  File "lxml.etree.pyx", line 3157, in lxml.etree.tostring (src\lxml\lxml.etree.c:69346)
  File "serializer.pxi", line 97, in lxml.etree._tostring (src\lxml\lxml.etree.c:114027)
  File "serializer.pxi", line 25, in lxml.etree._findOutputMethod (src\lxml\lxml.etree.c:113410)
ValueError: unknown output method 'test'
>>> lxml.etree.tostring(test,method="text")
b'HelloWorld'
>>> lxml.etree.tostring(test,method="html")
b'<html><head></head><body><p>Hello<br>World</p></body></html>'
>>> print(lxml.etree.tostring(test, method='html', pretty_print=True))
b'<html>\n<head></head>\n<body><p>Hello<br>World</p></body>\n</html>\n'
>>> print(lxml.etree.tostring(test, method='html', pretty_print=True).decode("ascii"))
<html>
<head></head>
<body><p>Hello<br>World</p></body>
</html>

>>> br = next(test.iter('br'))
>>> br
<Element br at 0x2581288>
>>> br.tail = 'W\xf6rld'
>>> bt.tail
Traceback (most recent call last):
  File "<pyshell#627>", line 1, in <module>
    bt.tail
NameError: name 'bt' is not defined
>>> br.taol
Traceback (most recent call last):
  File "<pyshell#628>", line 1, in <module>
    br.taol
AttributeError: 'lxml.etree._Element' object has no attribute 'taol'
>>> br.tail
'Wörld'
>>> lxml.etree.tostring(br,method="text")
Traceback (most recent call last):
  File "<pyshell#630>", line 1, in <module>
    lxml.etree.tostring(br,method="text")
  File "lxml.etree.pyx", line 3157, in lxml.etree.tostring (src\lxml\lxml.etree.c:69346)
  File "serializer.pxi", line 99, in lxml.etree._tostring (src\lxml\lxml.etree.c:114048)
  File "serializer.pxi", line 71, in lxml.etree._textToString (src\lxml\lxml.etree.c:113840)
UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' in position 1: ordinal not in range(128)
>>> lxml.etree.tostring(br,method="text",encoding="utf-8")
b'W\xc3\xb6rld'
>>> print(lxml.etree.tostring(br,method="text",encoding="utf-8",pretty_print=True).decode("utf-8"))
Wörld
>>> print(lxml.etree.tostring(br,method="html",encoding="utf-8",pretty_print=True).decode("utf-8"))
<br>Wörld

>>>  print(lxml.etree.tostring(test,method="html",encoding="utf-8",pretty_print=True).decode("utf-8"))
 
SyntaxError: unexpected indent
>>> print(lxml.etree.tostring(test,method="html",encoding="utf-8",pretty_print=True).decode("utf-8"))
<html>
<head></head>
<body><p>Hello<br>Wörld</p></body>
</html>

>>> print(lxml.etree.tostring(test,method="html",encoding="unicode",pretty_print=True))
<html>
<head></head>
<body><p>Hello<br>Wörld</p></body>
</html>

>>> lxml.etree.tostring(test,method="html",encoding="unicode",pretty_print=True)
'<html>\n<head></head>\n<body><p>Hello<br>Wörld</p></body>\n</html>\n'
>>> lxml.etree.tostring(test,method="html",encoding="unicode")
'<html><head></head><body><p>Hello<br>Wörld</p></body></html>'
>>> root = lxml.etree.XML('''\
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<a>&tasty;</a>
</root>
''')
>>> root
<Element root at 0x2579fa8>
>>> root[0]
<Element a at 0x25810f8>
>>> tree = lxml.etree.ElementTree(root)
>>> tree
<lxml.etree._ElementTree object at 0x025812B0>
>>> tree.docinfo
<lxml.etree.DocInfo object at 0x02583250>
>>> tree.docinfo.xml_version
'1.0'
>>> tree.docinfo.doctype
'<!DOCTYPE root SYSTEM "test">'
>>> root
<Element root at 0x2579fa8>
>>> tree
<lxml.etree._ElementTree object at 0x025812B0>
>>> lxml.etree.tostring(tree)
b'<!DOCTYPE root SYSTEM "test" [\n<!ENTITY tasty "parsnips">\n]>\n<root>\n<a>parsnips</a>\n</root>'
>>> root = lxml.etree.fromstring('''\
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<a>&tasty;</a>
</root>
''')
>>> root
<Element root at 0x25815f8>
>>> root.tag
'root'
>>> lxml.etree.tostring(rot)
Traceback (most recent call last):
  File "<pyshell#655>", line 1, in <module>
    lxml.etree.tostring(rot)
NameError: name 'rot' is not defined
>>> lxml.etree.tostring(root)
b'<root>\n<a>parsnips</a>\n</root>'
>>> lxml.etree.parse(
KeyboardInterrupt
>>> import urllib.request
>>> u = urllib.request.urlopen('http://planet.python.org/rss20.xml')
>>> tree = lxml.etree.parse(u)
>>> tree
<lxml.etree._ElementTree object at 0x0252D328>
>>> tree.getroot()
<Element rss at 0x252d2b0>
>>> parser = lxml.etree.XMLParser(remove_blank_text=True)
>>> root = lxml.etree.XML('''\
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<a>&tasty;</a>
</root>
''',parser)
>>> lxml.etree.tostring(root)
b'<root><a>parsnips</a></root>'
>>> root = lxml.etree.XML('''
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<b>   </b>
<a>&tasty;</a>
</root>
''',parser)
KeyboardInterrupt
>>> root = lxml.etree.XML('''
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<b>   </b>
<a>&tasty;</a>
</root>
''',parser)
Traceback (most recent call last):
  File "<pyshell#667>", line 8, in <module>
    ''',parser)
  File "lxml.etree.pyx", line 3012, in lxml.etree.XML (src\lxml\lxml.etree.c:67876)
  File "parser.pxi", line 1786, in lxml.etree._parseMemoryDocument (src\lxml\lxml.etree.c:102470)
  File "parser.pxi", line 1667, in lxml.etree._parseDoc (src\lxml\lxml.etree.c:101229)
  File "parser.pxi", line 1035, in lxml.etree._BaseParser._parseUnicodeDoc (src\lxml\lxml.etree.c:96139)
  File "parser.pxi", line 582, in lxml.etree._ParserContext._handleParseResultDoc (src\lxml\lxml.etree.c:91290)
  File "parser.pxi", line 683, in lxml.etree._handleParseResult (src\lxml\lxml.etree.c:92476)
  File "parser.pxi", line 622, in lxml.etree._raiseParseError (src\lxml\lxml.etree.c:91772)
  File "<string>", line None
lxml.etree.XMLSyntaxError: XML declaration allowed only at the start of the document, line 2, column 6
>>> root = lxml.etree.XML('''\
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<b>   </b>
<a>&tasty;</a>
</root>
''',parser)
>>> root = lxml.etree.XML('''<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
<b>   </b>
<a>&tasty;</a>
</root>
''',parser)
>>> root
<Element root at 0x2544580>
>>> lxml.etree.tostring(root)
b'<root><b>   </b><a>parsnips</a></root>'
>>> not []
True
>>> not {}
True
>>> not ''
True
>>> parser = lxml.etree.XMLParser()
>>> parser = ET.XMLParser()
>>> parser.feed("<roo")
>>> parser.feed("t><")
>>> parser.feed("a/")
>>> parser.feed("><")
>>> parser.feed("/root>")
>>> root = parser.close()
>>> root
<Element 'root' at 0x0257BAB0>
>>> root.tag
'root'
>>> lxml.etree.tostring(root)
Traceback (most recent call last):
  File "<pyshell#685>", line 1, in <module>
    lxml.etree.tostring(root)
  File "lxml.etree.pyx", line 3165, in lxml.etree.tostring (src\lxml\lxml.etree.c:69414)
TypeError: Type 'xml.etree.ElementTree.Element' cannot be serialized.
>>> ET.tostring(root)
b'<root><a /></root>'
>>> import io
>>> some_file_like = io.StringIO("<root><a>data</a></root>")
>>> some_file_like
<_io.StringIO object at 0x02588080>
>>> for event,element in lxml.etree.iterparse(some_file_like):
	print("%s, %4s, %s" % (event, element.tag, element.text))

	
Traceback (most recent call last):
  File "<pyshell#692>", line 1, in <module>
    for event,element in lxml.etree.iterparse(some_file_like):
  File "iterparse.pxi", line 207, in lxml.etree.iterparse.__next__ (src\lxml\lxml.etree.c:126137)
  File "iterparse.pxi", line 192, in lxml.etree.iterparse.__next__ (src\lxml\lxml.etree.c:125862)
  File "iterparse.pxi", line 220, in lxml.etree.iterparse._read_more_events (src\lxml\lxml.etree.c:126313)
TypeError: reading file objects must return bytes objects
>>> u
<http.client.HTTPResponse object at 0x02583510>
>>> u.read(10)
b''
>>> some_file_like = io.BytesIO("<root><a>data</a></root>")
Traceback (most recent call last):
  File "<pyshell#695>", line 1, in <module>
    some_file_like = io.BytesIO("<root><a>data</a></root>")
TypeError: 'str' does not support the buffer interface
>>> some_file_like = io.BytesIO(b"<root><a>data</a></root>")
>>> for event,element in lxml.etree.iterparse(some_file_like):
	print("%s, %4s, %s" % (event, element.tag, element.text))

	
end,    a, data
end, root, None
>>> for event, element in etree.iterparse(some_file_like,
...                                       events=("start", "end")):
...     print("%5s, %4s, %s" % (event, element.tag, element.text))
SyntaxError: invalid syntax
>>> 
>>> for event, element in etree.iterparse(some_file_like,events=("start", "end")):
	print("%5s, %4s, %s" % (event, element.tag, element.text))

	
Traceback (most recent call last):
  File "<pyshell#703>", line 1, in <module>
    for event, element in etree.iterparse(some_file_like,events=("start", "end")):
NameError: name 'etree' is not defined
>>> for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
	print("%5s, %4s, %s" % (event, element.tag, element.text))

	
Traceback (most recent call last):
  File "<pyshell#705>", line 1, in <module>
    for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
  File "iterparse.pxi", line 207, in lxml.etree.iterparse.__next__ (src\lxml\lxml.etree.c:126137)
  File "iterparse.pxi", line 192, in lxml.etree.iterparse.__next__ (src\lxml\lxml.etree.c:125862)
  File "iterparse.pxi", line 223, in lxml.etree.iterparse._read_more_events (src\lxml\lxml.etree.c:126343)
  File "parser.pxi", line 1295, in lxml.etree._FeedParser.close (src\lxml\lxml.etree.c:98571)
  File "<string>", line None
lxml.etree.XMLSyntaxError: no element found
>>> some_file_like = io.BytesIO(b"<root><a>data</a></root>")
>>> for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
	print("%5s, %4s, %s" % (event, element.tag, element.text))

	
start, root, None
start,    a, data
  end,    a, data
  end, root, None
>>> some_file_like.tell()
24
>>> for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
	some_file_like.seek(0)
	print("%5s, %4s, %s" % (event, element.tag, element.text))

	
Traceback (most recent call last):
  File "<pyshell#711>", line 1, in <module>
    for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
  File "iterparse.pxi", line 207, in lxml.etree.iterparse.__next__ (src\lxml\lxml.etree.c:126137)
  File "iterparse.pxi", line 192, in lxml.etree.iterparse.__next__ (src\lxml\lxml.etree.c:125862)
  File "iterparse.pxi", line 223, in lxml.etree.iterparse._read_more_events (src\lxml\lxml.etree.c:126343)
  File "parser.pxi", line 1295, in lxml.etree._FeedParser.close (src\lxml\lxml.etree.c:98571)
  File "<string>", line None
lxml.etree.XMLSyntaxError: no element found
>>> def test(some_file_like):
	some_file_like.seek(0)
	for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
		print("%5s, %4s, %s" % (event, element.tag, element.text))

		
>>> some_file_like.tell()
24
>>> test(some_file_like)
start, root, None
start,    a, data
  end,    a, data
  end, root, None
>>> some_file_like.tell()
24
>>> def test(some_file_like):
	some_file_like.seek(0)
	for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
		print("%5s, %4s, %s" % (event, element.tag, element.text))
		if element.tag == 'a':
			element.clear()

			
>>> test(some_file_like)
start, root, None
start,    a, data
  end,    a, None
  end, root, None
>>> some_file_like.seek(0)
0
>>> some_file_like.read()
b'<root><a>data</a></root>'
>>> def test(some_file_like):
	some_file_like.seek(0)
	for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
		print("%5s, %4s, %s" % (event, element.tag, element.text))
		if element.tag == 'a':
			element.getparent().remove(element)

			
>>> test(some_file_like)
start, root, None
start,    a, data
  end,    a, data
Traceback (most recent call last):
  File "<pyshell#727>", line 1, in <module>
    test(some_file_like)
  File "<pyshell#726>", line 6, in test
    element.getparent().remove(element)
AttributeError: 'NoneType' object has no attribute 'remove'
>>> def test(some_file_like):
	some_file_like.seek(0)
	for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
		print("%5s, %4s, %s" % (event, element.tag, element.text))
		if element.tag == 'a' and event == "end":
			element.getparent().remove(element)
	some_file_like.seek(0)

	
>>> test(some_file_like)
start, root, None
start,    a, data
  end,    a, data
  end, root, None
>>> def test(some_file_like):
	some_file_like.seek(0)
	for event, element in lxml.etree.iterparse(some_file_like,events=("start", "end")):
		print("%5s, %4s, %s" % (event, element.tag, element.text))
		if element.tag == 'a' and event == "end":
			print("in remove")
			element.getparent().remove(element)
	some_file_like.seek(0)

	
>>> test(some_file_like)
start, root, None
start,    a, data
  end,    a, data
in remove
  end, root, None
>>> xml_file = BytesIO('''\
<root>
<a><b>ABC</b><c>abc</c></a>
<a><b>MORE DATA</b><c>more data</c></a>
<a><b>XYZ</b><c>xyz</c></a>
</root>''')
Traceback (most recent call last):
  File "<pyshell#735>", line 1, in <module>
    xml_file = BytesIO('''\
NameError: name 'BytesIO' is not defined
>>> xml_file = BytesIO('''\
<root>
<a><b>ABC</b><c>abc</c></a>
<a><b>MORE DATA</b><c>more data</c></a>
<a><b>XYZ</b><c>xyz</c></a>
</root>''')
Traceback (most recent call last):
  File "<pyshell#736>", line 1, in <module>
    xml_file = BytesIO('''\
NameError: name 'BytesIO' is not defined
>>> xml_file = io.BytesIO('''\
<root>
<a><b>ABC</b><c>abc</c></a>
<a><b>MORE DATA</b><c>more data</c></a>
<a><b>XYZ</b><c>xyz</c></a>
</root>''')
Traceback (most recent call last):
  File "<pyshell#737>", line 6, in <module>
    </root>''')
TypeError: 'str' does not support the buffer interface
>>> xml_file = io.BytesIO(b'''\
<root>
<a><b>ABC</b><c>abc</c></a>
<a><b>MORE DATA</b><c>more data</c></a>
<a><b>XYZ</b><c>xyz</c></a>
</root>''')
>>> xml_file
<_io.BytesIO object at 0x02558DC0>
>>> for _, element in lxml.etree.iterparse(xml_file,tag='a')
SyntaxError: invalid syntax
>>> for _, element in lxml.etree.iterparse(xml_file,tag='a'):
	print('%s -- %s' % (element.findtext('b'),element.findtext('c')))
	element.clear()

	
ABC -- abc
MORE DATA -- more data
XYZ -- xyz
>>> element
<Element a at 0x2581490>
>>> element.tag
'a'
>>> element.findtext('b')
>>> lxml.etree.tostring(element)
b'<a/>'
>>> def test(xml_file):
	xml_file.seek(0)
	for _, element in lxml.etree.iterparse(xml_file,tag='a'):
		print('%s -- %s' % (element.findtext('b'),element.findtext('c')))
		element.clear()
		lxml.etree.tostring(element)
	xml_file.seek(0)

	
>>> test(xml_file)
ABC -- abc
MORE DATA -- more data
XYZ -- xyz
>>> def test(xml_file):
	xml_file.seek(0)
	for _, element in lxml.etree.iterparse(xml_file,tag='a'):
		print('%s -- %s' % (element.findtext('b'),element.findtext('c')))
		print(lxml.etree.tostring(element))
		element.clear()
		print(lxml.etree.tostring(element))
	xml_file.seek(0)

	
>>> test(xml_file)
ABC -- abc
b'<a><b>ABC</b><c>abc</c></a>\n'
b'<a/>'
MORE DATA -- more data
b'<a><b>MORE DATA</b><c>more data</c></a>\n'
b'<a/>'
XYZ -- xyz
b'<a><b>XYZ</b><c>xyz</c></a>\n'
b'<a/>'
>>> parser
<xml.etree.ElementTree.XMLParser object at 0x0257E5D0>
>>> class MaxDepth():
	_maxDepth = 0
	_depth = 0
	def start(self,tag,attrib):
		self._depth += 1
		if self._depth > self._maxDepth
		
SyntaxError: invalid syntax
>>> class MaxDepth():
	_maxDepth = 0
	_depth = 0
	def start(self,tag,attrib):
		self._depth += 1
		if self._depth > self._maxDepth:
			self._maxDepth = self._depth
	def end(self,tag):
		self._depth -= 1
	def data(self,data):
		print("in data",data,type(data))
	def close(self):
		return self.__maxDepth

	
>>> target = MaxDepth()
>>> parser = ET.XMLParser(target=target)
>>> exampleXml = """
 <a>1
   <b>2
   </b>3
   <b>4
     <c>5
       <d>6
       </d>7
     </c>8
   </b>9
 </a>"""
>>> parser.feed(exampleXml)
in data 1 <class 'str'>
in data 
 <class 'str'>
in data     <class 'str'>
in data 2 <class 'str'>
in data 
 <class 'str'>
in data     <class 'str'>
in data 3 <class 'str'>
in data 
 <class 'str'>
in data     <class 'str'>
in data 4 <class 'str'>
in data 
 <class 'str'>
in data       <class 'str'>
in data 5 <class 'str'>
in data 
 <class 'str'>
in data         <class 'str'>
in data 6 <class 'str'>
in data 
 <class 'str'>
in data         <class 'str'>
in data 7 <class 'str'>
in data 
 <class 'str'>
in data       <class 'str'>
in data 8 <class 'str'>
in data 
 <class 'str'>
in data     <class 'str'>
in data 9 <class 'str'>
in data 
 <class 'str'>
in data   <class 'str'>
>>> 
KeyboardInterrupt
>>> parser.close()
Traceback (most recent call last):
  File "<pyshell#782>", line 1, in <module>
    parser.close()
  File "<pyshell#777>", line 13, in close
    return self.__maxDepth
AttributeError: 'MaxDepth' object has no attribute '_MaxDepth__maxDepth'
>>> class MaxDepth():
	_maxDepth = 0
	_depth = 0
	def start(self,tag,attrib):
		self._depth += 1
		if self._depth > self._maxDepth:
			self._maxDepth = self._depth
	def end(self,tag):
		self._depth -= 1
	def data(self,data):
		print("in data",bytes(data),type(data))
	def close(self):
		return self._maxDepth

	
>>> target = MaxDepth()
>>> parser = lxml.etree.XMLParser(target=target)
>>> parser.feed(exampleXML)
Traceback (most recent call last):
  File "<pyshell#787>", line 1, in <module>
    parser.feed(exampleXML)
NameError: name 'exampleXML' is not defined
>>> parser.feed(exampleXml)
Traceback (most recent call last):
  File "<pyshell#788>", line 1, in <module>
    parser.feed(exampleXml)
  File "parser.pxi", line 1155, in lxml.etree._FeedParser.feed (src\lxml\lxml.etree.c:98443)
  File "parser.pxi", line 1279, in lxml.etree._FeedParser.feed (src\lxml\lxml.etree.c:98326)
  File "parsertarget.pxi", line 136, in lxml.etree._TargetParserContext._handleParseResult (src\lxml\lxml.etree.c:112770)
  File "parsertarget.pxi", line 130, in lxml.etree._TargetParserContext._handleParseResult (src\lxml\lxml.etree.c:112677)
  File "lxml.etree.pyx", line 327, in lxml.etree._ExceptionContext._raise_if_stored (src\lxml\lxml.etree.c:10196)
  File "saxparser.pxi", line 498, in lxml.etree._handleSaxData (src\lxml\lxml.etree.c:107757)
  File "parsertarget.pxi", line 83, in lxml.etree._PythonSaxParserTarget._handleSaxData (src\lxml\lxml.etree.c:112105)
  File "<pyshell#784>", line 11, in data
    print("in data",bytes(data),type(data))
TypeError: string argument without an encoding
>>> class MaxDepth():
	_maxDepth = 0
	_depth = 0
	def start(self,tag,attrib):
		self._depth += 1
		if self._depth > self._maxDepth:
			self._maxDepth = self._depth
	def end(self,tag):
		self._depth -= 1
	def data(self,data):
		print("in data",bytes(data,"ascii"),type(data))
	def close(self):
		return self._maxDepth

	
>>> target = MaxDepth()
>>> parser = lxml.etree.XMLParser(target=target)
>>> parser.feed(exampleXml)
in data b'1\n   ' <class 'str'>
in data b'2\n   ' <class 'str'>
in data b'3\n   ' <class 'str'>
in data b'4\n     ' <class 'str'>
in data b'5\n       ' <class 'str'>
in data b'6\n       ' <class 'str'>
in data b'7\n     ' <class 'str'>
in data b'8\n   ' <class 'str'>
in data b'9\n ' <class 'str'>
>>> parser = lxml.etree.XMLParser(remove_blank_text=True,target=target)
>>> parser.feed(exampleXml)
in data b'1\n   ' <class 'str'>
in data b'2\n   ' <class 'str'>
in data b'3\n   ' <class 'str'>
in data b'4\n     ' <class 'str'>
in data b'5\n       ' <class 'str'>
in data b'6\n       ' <class 'str'>
in data b'7\n     ' <class 'str'>
in data b'8\n   ' <class 'str'>
in data b'9\n ' <class 'str'>
>>> root = parser.close()
>>> root
4
>>> class ParserTarget:
	events[]
	
SyntaxError: invalid syntax
>>> class ParserTarget:
	events = []
	close_count = 0
	def start(self,tag,attrib):
		self.events.append(('start',tag,attrib))
	def close(self):
		events,self.events = self.events,[]
		self.close_count += 1
		return events

	
>>> target = ParserTarget()
>>> parser = lxml.etree.XMLParser(target=target)
>>> parser
<lxml.etree.XMLParser object at 0x0256BD40>
>>> parser.feed(exampleXml)
>>> events = parser.close()
>>> events
[('start', 'a', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'b', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'b', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'c', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'd', <lxml.etree._ImmutableMapping object at 0x025085F0>)]
>>> events = lxml.etree.XML(exampleXml,parser)
>>> events
[('start', 'a', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'b', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'b', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'c', <lxml.etree._ImmutableMapping object at 0x025085F0>), ('start', 'd', <lxml.etree._ImmutableMapping object at 0x025085F0>)]
>>> parser.close_count
Traceback (most recent call last):
  File "<pyshell#818>", line 1, in <module>
    parser.close_count
AttributeError: 'lxml.etree.XMLParser' object has no attribute 'close_count'
>>> target.close_count
2
>>> import htmllib
Traceback (most recent call last):
  File "<pyshell#820>", line 1, in <module>
    import htmllib
ImportError: No module named 'htmllib'
>>> import htmlib
Traceback (most recent call last):
  File "<pyshell#821>", line 1, in <module>
    import htmlib
ImportError: No module named 'htmlib'
>>> 
