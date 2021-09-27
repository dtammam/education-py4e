'''
Escape Character
    If you want a special regular expression character to just behave normally (most of the time) you prefix it with \
'''

# I'd like to find all strings that start with a real dollar sign followed by at least one or more numbers or dots.
# [\S+@\S+]

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)