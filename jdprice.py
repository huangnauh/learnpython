#coding:utf-8

import urllib
import json
import re

 
 
class JdPrice(object):
    def __init__(self, url):
        self.url = url
        self._response = urllib.urlopen(self.url)
        self.html = self._response.read()
 
    def get_product(self):
        product_re = re.compile(r'compatible: true,(.*?)};', re.S)
        product_info = re.findall(product_re, self.html)[0]
        return product_info
 
    def get_skuid(self):
        product_info = self.get_product()
        skuid_re = re.compile(r'skuid: (.*?),')
        skuid = re.findall(skuid_re, product_info)[0]
        return skuid
        
    def get_price(self):
        price = None
        skuid = self.get_skuid()
        print skuid
        url = 'http://item.m.jd.com/ware/view.action?wareId='+skuid
        html = urllib.urlopen(url).read()
        price_re = re.compile(r'id="jdPrice" name="jdPrice" value="(\d+.\d\d)"')
        price = re.findall(price_re, html)[0]
        return price
 
if __name__ == '__main__':
    url = 'http://item.jd.com/1279804.html'
    jp = JdPrice(url)
    print jp.get_product_price()