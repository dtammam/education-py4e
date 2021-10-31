'''
Searching a String

    - We use the find() function to search for a substring within another string
    - find() finds the first occurrence of the substring
    - If the substring is not found, find() returns -1
    - Remember that string positions start at 0
'''
# b a n a n a
# 0 1 2 3 4 5

fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)