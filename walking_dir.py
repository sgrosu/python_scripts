#!/usr/bin/python
'''
Verbose directory walking script
'''

import os

path = '/home/sgrosu/python'

def enumerate_paths(path=path):
	''' returns the path to all files in a directory recursively '''
	path_collection = []
	for dirpath, dirnames, filenames in os.walk(path):
		#print dirpath
		for fil in filenames:
			#print file
			fullpath = os.path.join(dirpath,fil)
			path_collection.append(fullpath)
	return path_collection

def enumerate_files(path=path):
	''' returns all files in a directory as a list '''
	file_collection = []
	for dirpath, dirnames, filenames in os.walk(path):
		for fil in filenames:
			file_collection.append(dirpath+'/'+fil)
	return file_collection

def enumerate_dir(path=path):
	''' returns all the directories in a directory as a list '''
	dir_collection = []
	for dirpath, dirnames, filenames in os.walk(path):
		for _dir in dirnames:
			dir_collection.append(_dir)
	return dir_collection

if __name__ == "__main__":
	#print "\nRecursive listing of all paths in a dir:\n"
	#for paths in enumerate_paths():
	#	print path
	print "\nrecursive listing of all files in a dir:\n"
	for file in enumerate_files():
		print file
	#print "\nrecursive listing of all dirs in a dir:\n"
	#for diir in enumerate_dir():
	#	print diir


