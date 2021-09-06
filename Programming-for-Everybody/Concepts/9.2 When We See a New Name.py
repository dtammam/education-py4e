'''
When We See a New Name
    - When we encounter a new name, we need to add a new entry in the dictionary
    - If this is the second or later time we have seen the name, we simply add one to the count in the dictionary under that name
'''

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)