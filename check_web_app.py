#!/home/sgrosu/anaconda2/bin/python

import socket
import re
import sys

def check_webserver(address,port,resource=''):
	# buid uop an HTTP request string
	if not resource.startswith('/'):
		resource = '/' + resource
	request_string = 'GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (resource,address)
	print 'HTTP request:'
	print '||| %s |||' % request_string

	# create a TCP socket
	s = socket.socket()
	print 'attempting to conect to %s on port %s' % (address,port)
	try:
		s.connect((address,port))
		print 'conencted to %s on port %s' % (address,port)
		s.send(request_string)
		# we only need the first 100 bytes or so
		rsp = s.recv(200)
		print 'received 200 bytes of HTTP response'
		print '||| %s |||' % rsp
	except socket.error, e:
		print 'connection to % s on port %s failed: %s' % (address,port,e)
		return False
	finally:
		# close the connection
		s.close()
	lines = rsp.splitlines()
	print 'first line of response: %s' % lines[0]
	try:
		version, status, message = re.split('\s+',lines[0],2)
	except ValueError as ve:
		print 'failed to split status line: ', ve
		return False
	if status in ['200','301']:
		print 'Success! Status was %s' % status
		return True
	else:
		print 'status was %s' % status
		return False


check_webserver('sebastiangrosu.com',80)
