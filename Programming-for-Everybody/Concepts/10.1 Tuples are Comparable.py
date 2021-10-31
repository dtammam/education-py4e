'''
Tuples are Comparable

    - The comparison operators work with tuples and other sequences
    - If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ
'''
# True because 0 < 5
print((0, 1, 2) < (5, 1, 2))

# True because 1 < 3
print((0, 1, 2000000) < (0, 3, 4))

# True because l in Sally is < m
print(('Jones', 'Sally') < ('Jones', 'Sam'))

# True because J in Jones is > A
print(('Jones', 'Sally') > ('Adams', 'Sam'))