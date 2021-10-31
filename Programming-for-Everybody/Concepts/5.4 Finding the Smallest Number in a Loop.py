'''
Finding the Smallest Number in a Loop

    - The opposite is NOT true. We won't find the smallest starting with a positive number
    - We use the None keyword to start it as null, then the first number becomes the smallest so far
'''
smallest = None
print('Before', smallest)

for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None : 
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)

print('After', smallest)