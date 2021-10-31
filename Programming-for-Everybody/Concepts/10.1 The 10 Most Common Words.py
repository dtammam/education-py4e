'''
The 10 Most Common Words

    - With dictionaries, we easily find the most commonly used word.
    - Using dictionaries, temporary lists and tuples, we can find the most common words.
'''
# This block opens a file and creates a dictionary which effectively produces a histogram of all words, counted in no particular order.
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# This block extracts the data out of the dictionary using a for loop that uses a value/key tuple and append to a new temporary list. A list of tuples in value, key order.
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

# Now, let's sort that backwards, from the highest value down to the lowest value.
lst = sorted(lst, reverse=True)

# The list is now backwards. Slice, starting at the beginning and going upto but not including the last one. Then print out the way we wanted to in the first place.
for val, key in lst[:10]:
    print(key, val)