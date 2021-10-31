'''
A Tale of Two Loops

    - We can use our old school basic loop with for/in to get a result printed. But what if the position ever mattered?
    - Our first loop is an example of the basic loop.
    - Our second loop uses a constructed index loop using for and an integer iterator, and we can print based off of the index for our typical result.
'''
friends = ['Ray', 'Julian', 'Mont']

# First Loop
for friend in friends :
    print('Why hello there,', friend)

# Second Loop
for i in range(len(friends)) :
    friend = friends[i]
    print('Why hello there,', friend)