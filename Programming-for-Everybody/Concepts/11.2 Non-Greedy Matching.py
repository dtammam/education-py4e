'''
Non-Greedy Matching
    - Not all regular expression repeat codes are greedy!
    - If you add a ? character, the + and * chill out a bit…
'''

# I'm looking for lines that start with F followed by one or more characters while not being greedy, with the last character being a colon.
# [^F.+?:]

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)