#!/home/sgrosu/anaconda2/bin/python

import urllib
import requests
import time

url = 'http://winonaesolutions.co.uk'
nf = urllib.urlopen(url)
start = time.time()
print start
page = nf.read()
end = time.time()
print end
nf.close()

print 'page load time was %.2f seconds' % (end - start)
print 'the other method shows: %.2f seconds' % requests.get(url).elapsed.total_seconds()