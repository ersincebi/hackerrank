import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
	return sum([len(elem.items()) for elem in tree.iter()])
	




if __name__ == '__main__':
	xml = "<feed xml:lang='en'>  <title>HackerRank</title>  <subtitle lang='en'>Programming challenges</subtitle>  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>  <updated>2013-12-25T12:00:00</updated>  <entry>  	<author gender='male'>Harsh</author>    <question type='hard'>XML 1</question>    <description type='text'>This is related to XML parsing</description>  </entry></feed>"
	tree = etree.ElementTree(etree.fromstring(xml))
	root = tree.getroot()
	print(get_attr_number(root))