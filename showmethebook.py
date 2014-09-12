#!E:/python27/python.exe
#  coding=utf-8

from selenium import webdriver
import time
fp = webdriver.FirefoxProfile('C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/lf7fh0d5.default')
wd = webdriver.Firefox(fp)
wd.get("http://www.duokan.com/reader/www/app.html?id=e5e31c0afc15430fab5d49c038b2a18b")  # 换成书的在线阅读地址

pagecount = 860   # 换成书的总页数
content = ''
for i in range(320, pagecount / 2 + 1):
	wd.execute_script("$('.u-layer .j-close').trigger('click')")
	while wd.execute_script("return $('#book_page_%s text').length" % str(i * 2)) == 0 and wd.execute_script("return $('#book_page_%s .text').length" % str(i * 2)) == 0:
		time.sleep(1)
	content += wd.execute_script("var content = '';$('#book_page_%s text').each(function(){content += $(this).text()});return content;" % str(i * 2))
	if i * 2 + 1 > pagecount:
		break
	content += wd.execute_script("var content = '';$('#book_page_%s text').each(function(){content += $(this).text()});return content;" % str(i * 2 + 1))
	wd.execute_script("$('.j-pagedown').trigger('click')")
wd.close()
with open('book.html', 'w') as f:
	f.write(content.encode('utf-8'))