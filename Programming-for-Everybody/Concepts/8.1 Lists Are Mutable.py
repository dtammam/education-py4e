'''
Lists Are Mutable

    - Strings are 'immutable' - we cannot change the contents of a string. We must make a new string to make any change.
    - Lists are 'mutable' - we can change an element of a list using the index operator
'''
fruit = 'Banana'

# This code would fail for a string
# fruit[0] = 'b'
# TypeError: 'str' object does not support item assignment

x = fruit.lower()
print(x)

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)