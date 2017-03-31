from xml.etree import ElementTree as ET

books = ET.parse('books.xml')
#print books

#first_book = books.find('/book')

#print first_book

#print first_book.attrib

root = books.getroot()
print root.attrib

for child_of_root in root:
	print child_of_root.attrib
	for elem in child_of_root:
		print elem.tag, ': ', elem.text
