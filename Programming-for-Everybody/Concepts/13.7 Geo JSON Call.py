'''
GeoJSON Call

    - See below for almost a full lifecycle of a GeoJSON API call to Google
    - We call Google APIs, pass information and get it back
    - We are missing API keys and a potential dictionary to pass multiple parameters
'''
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode.json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print('===== Failure To Retrieve =====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)