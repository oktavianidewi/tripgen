from urllib2 import Request,urlopen, URLError
import json

auth_key = 'AIzaSyDhKlyoA5Aq8DrZ9mM3e3RHQYkDv8a8AcQ'
# location = '-7.9716403,112.6317838' # malang
# location = '-7.6060768,110.2196545' # jogja
# location = '-7.2574719,112.7520883' # surabaya
# location = '-6.9174639,107.6191228' # bandung
location = '-6.2087634,106.845599' # jakarta

radius = '5000' # satuannya apa ya? meter
url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s&radius=%s') %(auth_key, location, radius)
# response = urllib2.urlopen(url)
print url
# quit()
try:
    request = Request(url)
    response = urlopen(request)
    # json_raw = response.read()
    json_data = response.read()
    print json_data
    """
    if json_data['status'] == 'OK':
        for place in json_data['result']:
            print '%s: %s\n' %(place['name'], place['reference'])
    """
except URLError, e:
    print 'Got an error: ', e

# https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters
# https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s&radius=%s
# https://maps.googleapis.com/maps/api/place/search/json?location=%s&radius=%s&sensor=false&key=%s