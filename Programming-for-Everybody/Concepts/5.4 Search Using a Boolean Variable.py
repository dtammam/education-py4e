found = 'Not Detected'
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = 'Detected'
    print(found, value)
print('After', found)