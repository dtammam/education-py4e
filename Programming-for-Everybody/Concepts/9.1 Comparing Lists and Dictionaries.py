'''
Comparing Lists and Dictionaries
    - Dictionaries are like lists except that they use keys instead of numbers to look up values
    - Its' the difference between labels and positions
'''

# A list, that does the same thing as the dictionary below
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

# A dictionary, that does the same thing as the list above
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)