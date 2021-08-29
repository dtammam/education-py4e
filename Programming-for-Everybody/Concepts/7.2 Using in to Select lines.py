'''
Using in to Select lines
    - We can look for a string anywhere in a line as our selection criteria
'''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not 'uct.ac.za' in line :
        continue
    print(line)