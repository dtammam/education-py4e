'''
Stripping Whitespace
    - Sometimes we want to take a string and remove whitespace at the beginning and/or end
    - lstrip() and rstrip() remove whitespace at the left or right
    - strip() removes both beginning and ending whitespace
'''

greet = '     Hello, Bob!       '
print(greet)
greet.lstrip()
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())