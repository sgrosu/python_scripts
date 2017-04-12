#!/usr/bin/python
''' API for getting directory walk collections '''

import os

class diskwalk(object):

	def __init__(self,path):
		self.path = path

	def enumeratePaths(self):
		''' returns the path to all the files in a directory as a list '''
		path_collection = []
		for dirpath, dirnames, filenames in os.walk(self.path):
			for fil in filenames:
				fullpath = os.path.join(dirpath,fil)
				path_collection.append(fullpath)
		return path_collection

	def enumerateFiles(self):
		''' returns all the files in a directory as a list '''
		file_collection = []
		for dirpath, dirnames, filenames in os.walk(self.path):
			for fil in filenames:
				file_collection.append(fil)
		return file_collection

	def enumerateDir(self):
		''' returns all the directories in a directory as a list '''
		dir_collector = []
		for dirpath, dirnames, filenames in os.walk(self.path):
			for di in dirnames:
				dir_collector.append(di)
		return dir_collector

	def fileNumber(self):
		''' returns the number of files in directory '''
		return len(self.enumerateFiles())

#p = diskwalk('/home/sgrosu')

#print p.fileNumber()


