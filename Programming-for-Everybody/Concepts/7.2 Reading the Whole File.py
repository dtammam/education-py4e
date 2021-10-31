'''
Reading the Whole File

    - We can read the whole file (newlines and all) into a single string
'''
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])