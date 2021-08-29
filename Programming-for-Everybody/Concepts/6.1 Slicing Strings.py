'''
Slicing Strings
    - We can also look at any continuous section of a string using a colon operator
    - The second number is one beyond the end of the slice - "up to but not including"
    - If the second number is beyond the end of the string, it stops at the end
    - If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
'''

# M o n t y   P y t h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

t = 'Mommy Dearest'
print(t[:2])
print(t[8:])
print(t[:])

print(len('training'))