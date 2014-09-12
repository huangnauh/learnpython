__author__ = 'huanglibo'

import htmllib
import formatter
import string
import sgmllib


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

if __name__ == "__main__":
    testSgml()