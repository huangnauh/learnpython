import os
import sys
import string
import htmllib
import urllib
import urlparse
import formatter
import cStringIO

class Retriever(object):
	def __init__(self,url):
		self.url = url
		self.file = self.filename(url)
	def filename(self,url,deffile="index.htm"):
		parsedurl = urlparse.urlparse(url,"http:",0)
		path = parsedurl[1]+parsedurl[2]
		ext = os.path.splitext(path)
		if ext[1] == "":
			if path[-1] == "/":
				path += deffile
			else:
				path += '/' + deffile
		ldir = os.path.dirname(path)
		if os.sep != '/':
			ldir = string.replace(ldir, '/', os.sep)
			if not os.path.isdir(ldir):
				if os.path.exists(ldir):
					os.unlink(ldir)
				os.makedirs(ldir)
		return path
	def download(self):
		try:
			retval = urllib.urlretrieve(self.url,self.file)
		except IOError:
			retval = ('*** ERROR: invalid URL "%s"' % self.url)
		return retval
	def parseAndGetLinks(self):
		self.parser = htmllib.HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
		self.parser.feed(open(self.file).read())
		self.parser.close()
		return self.parser.anchorlist
	
class Crawler(object):
	count = 0
	def __init__(self, url): 
		self.q = [url]
		self.seen = []
		self.dom = urlparse.urlparse(url)[1]
	def getPage(self, url): 
		r = Retriever(url)
		retval = r.download() 
		if retval[0] == '*':
			print retval, '... skipping parse' 
			return
		Crawler.count += 1
		print '\n(', Crawler.count, ')' 
		print 'URL:', url
		print 'FILE:', retval[0]
		self.seen.append(url) 
		links = r.parseAndGetLinks()
		for eachLink in links: 
			if eachLink[:4] != 'http' and \
			string.find(eachLink, '://') == -1: 
				eachLink = urlparse.urljoin(url, eachLink)
				print '* ', eachLink,
			if string.find(string.lower(eachLink), 'mailto:') != -1:
				print '... discarded, mailto link' 
				continue
			if eachLink not in self.seen:
				if string.find(eachLink, self.dom) == -1: 
					print '... discarded, not in domain' 
				else:
					if eachLink not in self.q: 
						self.q.append(eachLink) 
						print '... new, added to Q' 
					else:
						print '... discarded, already in Q'
			else: 
				print '... discarded, already processed' 
			
	def go(self):
		while self.q:
			url = self.q.pop()
			self.getPage(url)
	
def main(): 
	try: 
		url = raw_input('Enter starting URL: ') 
	except (KeyboardInterrupt, EOFError):
		url = ''
	if not url:
		return 
	robot = Crawler(url)
	robot.go() 

if __name__ == '__main__': 
	main()