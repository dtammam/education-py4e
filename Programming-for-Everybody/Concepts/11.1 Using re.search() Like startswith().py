'''
Using re.search() Like startswith()

    - Before you can use regular expressions in your program, you must import the library using "import re"
    - We fine-tune what is matched by adding special characters to the string
'''
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:') :
#         print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)