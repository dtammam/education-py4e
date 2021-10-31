'''
Best Friends, Strings and Lists

    - Split breaks a string into parts and produces a list of strings.
    - We think of these as words.
    - We can access a particular word or loop through all the words.
'''
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)