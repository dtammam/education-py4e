'''
Following Links in Python

    In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
    
    We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
    
    1. Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
        - Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
        - Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
        - Last name in sequence: Anayah
    2. Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Kelsay.html
        - Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
        - Hint: The first character of the name of the last page that you will load is: A

    Strategy
        The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. 
        The point is to write a clever Python program to solve the program.

    Here is a sample execution of a solution:
        $ python3 solution.py
        Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
        Enter count: 4
        Enter position: 3
        Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
        Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
        Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
        Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
        Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
        The answer to the assignment for this execution is "Anayah".
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Set starting webpage
url = 'http://py4e-data.dr-chuck.net/known_by_Kelsay.html'
# Set how many times we need to loop through
count = int(input('Input count: '))
# Set the position we're shooting for, subtracting 1 for the starting position
position = int(input('Input position: ')) - 1

# Loop through, opening a page and setting the proper positional URL as the new one, then print and continue for the total number of counts remaining
while count > 0 :
    count -= 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get('href', None)
    print('Retrieving: ', url)