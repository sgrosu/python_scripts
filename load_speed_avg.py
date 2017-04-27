#!/home/sgrosu/anaconda2/bin/python

from __future__ import division
import requests
import time
import sys
import datetime
import socket


if len(sys.argv) < 2:
	url = 'http://winonaesolutions.co.uk'
else:
	if not sys.argv[1].startswith('http://'):
		url = 'http://'+ sys.argv[1]
	else:
		url = sys.argv[1]


def getIP(d):
    """
    This method returns the first IP address string
    that responds as the given domain name
    """
    try:
        data = socket.gethostbyname(d)
        ip = repr(data)
        return ip
    except Exception:
        # fail gracefully!
        return False
print url
print getIP(url.strip('http://'))
rezlist = []
for i in range(10):
    thetime = requests.get(url).elapsed.total_seconds()
    rezlist.append(thetime)
    print  '%s - TTFB: %.2f seconds' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),thetime)
    time.sleep(10)
average = (sum(rezlist) / float(len(rezlist)))
print rezlist
print 'average TTFB: %.2f' % average
print 'bye'
exit(0)