'''
Tuples Are Immutable
    - Unlike a list, once you create a tuple, you cannot alter its contents
    - It is similar to a string in this way
'''

# Lists are mutable
x = [9, 8, 7]
x[2] = 6
print(x)

# Strings are not mutable
y = 'ABC'
y[2] = 'D'

# Tuples are not mutable
z = (5, 4, 3)
z[2] = 0