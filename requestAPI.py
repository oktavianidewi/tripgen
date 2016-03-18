import urllib2
url = 'http://www.google.com'
try:
    result = urllib2.urlopen(url)
    read = result.read()
    print read
except URLError, e:
    print 'got error code'