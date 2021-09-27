'''
Fine-Tuning String Extraction
    - You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parenthesis
    - Parenthesis are not part of the match, but they tell where to start and stop what string to extract
'''

# I'd like to find all instances of an @ symbol with at least one non-whitespace character before and after it, like an email address. I want it greedy because I want all up-to spaces, for example d@u is not useful.
# [\S+@\S+]

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Please extract this only!
y = re.findall('\S+@\S+',x)
print(y)

#Please match starting at From, but extract only for the email!
y = re.findall('^From (\S+@\S+)',x)
print(y)