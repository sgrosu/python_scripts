#!/usr/bin/python

import os

class Delete(object):

	'''Delete methods for file objects'''
	def __init__(self,file):
		self.file = file

	def interactive(self):
		'''Interactive deletion mode'''
		input = raw_input("Do you really want to delete %s [N]/Y" % self.file[0])
		if input.upper() == 'Y':
			print "Deleting: %s" % self.file[0]
			status = os.remove(self.file[0])
		else:
			print "Skipping: %s" % self.file[0]
		return

	def dryrun(self):
		'''Simulation mode for deletion'''
		print "Dry run: %s [Not deleted]" % self.file[0]
		return

	def delete(self):
		'''Performs a delete on a file, with additional conditions'''
		print "Deleting: %s" % self.file
		try:
			status =  os.remove(self.file)
		except Exception, err:
			print err
			return status

if __name__ == "__main__":
	from duplicates import findDupes
	dupes = findDupes('/tmp/dirB')
	for dupe in dupes:
		delete = Delete(dupe)
		#delete.dryrun()
		#delete.delete()
		delete.interactive()