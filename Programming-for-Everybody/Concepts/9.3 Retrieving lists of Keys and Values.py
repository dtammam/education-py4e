'''
Retrieving lists of Keys and Values
    - You can get a list of keys, values or items (both) from a dictionary
'''

jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100 }

# Printing as a list shows a list of keys.
print(list(jjj))

# Printing as keys shows a list of keys.
print(jjj.keys())

# Printing as values shows a list of values.
print(jjj.values())

# Printing as items shows both, tuples!
print(jjj.items())