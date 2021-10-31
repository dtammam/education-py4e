'''
Matching and Extracting Data

	- re.search() returns a True/False depending on whether the string matches the regular expression
    - If we actually want the matching strings to be extracted, we use re.findall()
'''
# I want to take a line and extract at least one numeric digit.
# [0-9]+

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

# I want to take a line and extract at least one uppercase vowel.
# [AEIOU]+

y = re.findall('[AEIOU]+', x)
print(y)