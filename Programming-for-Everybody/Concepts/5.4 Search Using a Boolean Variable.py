'''
Search Using a Boolean Variable

    - This works by setting a string beforehand and then modifying that string during the loop
    - Once detected, we can use that in our results as an easy way to read it
'''
found = 'Not Detected'
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = 'Detected'
    print(found, value)
print('After', found)