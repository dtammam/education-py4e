'''
Even Cooler Regex Version

    - Things can be done multiple ways.
    - In certain instances, regex can do things more elegantly
'''
# We can fine tune this!
# I want to start with From in the line with a space and any number of characters upto an @ and I want to begin extracting all the non-blank characters, and then stop extracting.
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',line)
print(y)