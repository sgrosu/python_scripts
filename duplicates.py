#!/usr/bin/python
'''
Compare two directories by using md5 hashes
'''
import os
from walk_module import diskwalk
from md5_compare import create_checksum


def findDupes(path='/tmp/dirB'):

	d = diskwalk(path)
	files = d.enumeratePaths()

	dup = []
	record = {}

	for fil in files:
		compound_key = ((os.path.getsize(fil),create_checksum(fil)),fil)
		#print compound_key
		#print compound_key[:1][0]
		if compound_key[:1][0] in record:
			dup.append((record[compound_key[0]],fil))
			#dup.append(fil)
		else:
			#print compound_key[0]
			record[compound_key[0]] = fil
	return dup

if __name__ == "__main__":
	#print "Working in %s" % path
	dupes = findDupes()
	for dup in dupes:
		print "%s is a duplicate of %s" % (dup[0],dup[1])

#print record