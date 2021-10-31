'''
Using re.search() Like find()

   - Before you can use regular expressions in your program, you must import the library using "import re"
    - You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
    - You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]
'''
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)