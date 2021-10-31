'''
Finding the Largest Number in a Loop

    - This works by starting with a negative number
    - As we loop through, we continually check the number versus the last largest
    - The first to be found will always be larger than a negative
'''
largest_so_far = -1
print('The largest at the beginning is an itty bitty negative number', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print('The largest so far is', largest_so_far, 'after checking against', the_num)

print('The largest at the end is a much larger number', largest_so_far)