'''
Calling a JSON API

    In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
    
    API End Points
        To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

        http://py4e-data.dr-chuck.net/json?
        This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
        To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

        Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

    Test Data / Sample Execution
        You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJLzabHQ7i2IgRzeZb_AgUj0Q".

        $ python3 solution.py
        Enter location: South Federal University
        Retrieving http://...
        Retrieved 2146 characters
        Place id ChIJLzabHQ7i2IgRzeZb_AgUj0Q

    Turn In
        Please run your program to find the place_id for this location:
            Universidad de Buenos Aires
        Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJE1b ..."
        Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.
'''
# Import relevant modules
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Set the URL for our API pull
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create our while loop for the magic to happen. Using to allow for 'break'
while True:

    # Prompt for the location that we want a place_id for
    address = input('Enter location: ')

    # Provide API key
    apikey = 42

    # Fail out if no address is entered
    if len(address) < 1: break

    # Create a dictionary to pass parameters onto the URL
    params = dict()
    params['address'] = address
    params['key'] = apikey
    url = serviceurl + urllib.parse.urlencode(params)

    # Retrieve the URL, then print character counts in the .JSON file
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # Load the data, parse the 'results' top-level object and print out the 'place_id' for this location 
    # Once done, exit
    try:
        js = json.loads(data)
        print('Place id', js['results'][0]['place_id'])
        break
   
    # If we can't open .JSON, set the variable as None for error handling
    except:
        js = None

    # Notify user of failure if .JSON is not opened, there is no 'status' entry or the 'status' entry is not okay
    # Continue to allow a new address to be input
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue