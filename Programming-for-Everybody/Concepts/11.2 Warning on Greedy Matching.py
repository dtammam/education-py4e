'''
Warning: Greedy Matching

    - The repeat characters * and + push outward in both directions (greedy) to match the largest possible string
    - It will deliberately look for the biggest use of the condition instead of the first 'correct' one
'''
# I'm looking for lines that start with F followed by one or more characters with the last character being a colon.
# [^F.+:]

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)