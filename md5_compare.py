#!/usr/bin/python
'''
compare files by useing MD5 checksums
'''

import hashlib

def create_checksum(path):
	''' reads a file. creates a checksum of the file line by line
		returns complete checksum for file
	'''
	fp = open(path)
	checksum = hashlib.md5()
	while True:
		buf = fp.read(8192)
		if not buf: break
		checksum.update(buf)
	fp.close()
	checksum = checksum.digest()
	return checksum

#print create_checksum('/tmp/file0.txt') == create_checksum('/tmp/file1.txt')