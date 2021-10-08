'''
Treating Like a File
    - It only takes a few lines of code to take a web page and roll it into a simple import statement
    - If you think about things as files, you can easily handle data on the internet
    - A webpage is an internet 'file'
'''

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    # We need to decode it before we get it, it's a byte string versus a character string
    # All string methods will work on it after we decode
    # We only decode once
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)