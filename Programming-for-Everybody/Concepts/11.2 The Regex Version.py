'''
The Regex Version

    - Things can be done multiple ways.
    - In certain instances, regex can do things more elegantly
'''
# For reference, how we can use find and string slicing without regex for pulling a host!
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# at = data.find('@')
# space = data.find(' ',at)
# host = data[at+1 : space]
# print(host)

# And double-split pattern!
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# words = data.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])

# The regex version stands strong!
# Go find me an @ sign followed by some number of non-blank characters. I don't want to extract the @ sign, I want to extract afterwards.
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)',line)
print(y)