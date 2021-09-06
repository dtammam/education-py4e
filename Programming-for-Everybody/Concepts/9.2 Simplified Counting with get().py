'''
Simplified Counting with get()
    - We can use get() and provide a default value of zero when the key is not in the dictionary… and then just add one
'''

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)