#!/home/sgrosu/anaconda2/bin/python

import socket
import re
import sys

def check_server(address,port):
	# create a TCP socket
	s = socket.socket()
	print 'attempting to conect to %s on port %s' % (address,port)
	try:
		s.connect((address,port))
		print 'conencted to %s on port %s' % (address,port)
		return True
	except socket.error, e:
		print 'connection to % s on port %s failed: %s' % (address,port,e)
		return False

check_server('172.25.164.200',22)
