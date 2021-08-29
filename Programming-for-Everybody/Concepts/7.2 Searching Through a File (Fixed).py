'''	
Searching Through a File (fixed)
		- We can strip the whitespace from the right-hand side of the string using rstrip() from the string library
        - The newline is considered "white space" and is stripped 
'''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)