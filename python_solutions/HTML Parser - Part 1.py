from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Start : {0}".format(tag))
		for key, val in attrs:
			print("-> {0} > {1}".format(key, val))
	def handle_endtag(self, tag):
		print("End   : {0}".format(tag))
	def handle_startendtag(self, tag, attrs):
		print("Empty : {0}".format(tag))
		for key, val in attrs:
			print("-> {0} > {1}".format(key, val))
parser = MyHTMLParser()
lines = []
n = int(input())
for i in range(n):
	lines.append(str(input()).strip())
parser.feed(''.join(lines))