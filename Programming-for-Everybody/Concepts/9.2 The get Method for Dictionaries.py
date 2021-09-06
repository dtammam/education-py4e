'''
The get Method for Dictionaries
    - The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for it.
    - Default value if key does not exist (and no Traceback.
'''

if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)