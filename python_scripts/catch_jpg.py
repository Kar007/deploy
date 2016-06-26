#!/usr/bin/python

import urllib
import re

def getHtml(url):
	try:
		data = urllib.urlopen(url)
		html = data.read()
		data.close()
	except Exception,e:
		print ('Error information: %s' % e)
	
	return html

def getJpg(html):
	urllist = re.findall('img to="(http:.+?\.jpg)"', html)
	print urllist
	i = 1
	for url in urllist:
		print 'Downloading jpg: <%s>' % url
		urllib.urlretrieve(url,'%d.jpg' % i)
		i += 1



if __name__ == '__main__':
	html = getHtml('http://www.lvmama.com/')
	getJpg(html)
