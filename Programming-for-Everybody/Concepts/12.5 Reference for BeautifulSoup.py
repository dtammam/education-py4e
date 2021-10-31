'''
Reference for BeautifulSoup

    - The TCP/IP gives us pipes/sockets between applications
	- We designed application protocols to make use of these pipes
	- HyperText Transfer Protocol (HTTP) is a simple yet powerful protocol
    - Python has good support for sockets, HTTP, and HTML parsing
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# Try this URL
# http://www.dr-chuck.com/page1.htm

url = input('http://www.dr-chuck.com/page1.htm')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))