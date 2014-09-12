import urllib
import xml.etree.ElementTree
import collections
import lxml.etree

def test1():
	u = urllib.urlopen("http://planet.python.org/rss20.xml")
	doc = xml.etree.ElementTree.parse(u)
	root = doc.getroot()
	for item in doc.iterfind("channel/item"):
		title = item.findtext("title")
		data = item.findtext("pubDate")
		link = item.findtext("link")
		print(title,data,link)
	
def parse_and_remove(filename,path):
	path_parts = path.split('/')
	try:
		path_parts.remove('.')
	except ValueError:
		pass
	try:
		path_parts.remove('')
	except ValueError:
		pass
	plen = len(path_parts)
	doc = xml.etree.ElementTree.iterparse(filename,('start','end'))
	next(doc)
	tag_stack = []
	elem_stack = []
	for event, elem in doc:
		if event == "start":
			tag_stack.append(elem.tag)
			elem_stack.append(elem)
		elif event == "end":
			if tag_stack[-plen:] == path_parts:
				yield elem
				elem_stack[-2].remove(elem)
			try:
				tag_stack.pop()
				elem_stack.pop()
			except IndexError:
				pass
	

def test():
	print("in test")
	file_names = collections.Counter()
	doc = xml.etree.ElementTree.parse("0.xml")
	print(doc)
	for file in doc.iterfind(".//files/file"):
		file_names[file.findtext("name")] += 1
	for name,num in file_names.most_common(10):
		print(name,num)

def mytest():
	file_names = collections.Counter()
	data = parse_and_remove('0.xml', './/files/file')
	for file in data:
		file_names[file.findtext('name')] += 1
	for name,num in file_names.most_common(10):
		print(name,num)
	
def test0():
	html = lxml.etree.Element("html")
	body = lxml.etree.SubElement(html,"body")
	body.text = "TEXT"
	br = lxml.etree.SubElement(body,"br")
	br.tail="TAIL"
	lxml.etree.tostring(html)
	html.xpath("//text()")
	html.xpath("string()")
	foo = lxml.etree.XPath("//text()")
	print(foo(html))
	
test0()