'''
Reading Web Pages

    - We don't need to only read text files, we can read HTML files!
    - Just get the HTML file and write a loop!
    - We've written a web browser in 4 lines of code :)
    - Headers are here, we need to ask for them in a different way
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())