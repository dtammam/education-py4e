'''
More about Split

    - Splits by default on whitespace and treats more than one space as a single space
    - It doesn't have to work with spaces
    - .split('delimercharacter')
'''
line = 'A lot          of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))