'''
Tuples Are More Efficient

    - Methods for lists that tuples don't have make changes
    - Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists
    - So in our program when we are making temporary variables, we prefer tuples over lists
'''
l = list()
print(dir(l))

t = tuple()
print(dir(t))