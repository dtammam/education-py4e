'''
Skipping with Continue

    - We can conveniently skip a line by using the continue statement
    - Skipping what we're not interested in
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)