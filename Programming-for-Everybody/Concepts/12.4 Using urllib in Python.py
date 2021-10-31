'''
Using urllib in Python

    - Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file
    - Skips the headers, they can be opened afterwards if we are interested
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())