'''
Looping Through Strings With While

    - We can loop through a string the same way we loop through other things!
    - In our example below, we are adding to an index variable until we get to the end of our string
'''
fruit = 'banana'
index = 0
while index < len(fruit):
    x = fruit[index]
    print(index, x)
    index = index + 1