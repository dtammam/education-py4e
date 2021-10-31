'''
Prompting for Numbers and Calculating Average

    - This is a good demonstration of what this would look like with our easy-to-use built-in functions.
    - We don't need to construct the full on loops like we did in the past.
'''
# Old way which works but isn't entirely necessary. Important at scale as it only holds one number and two variables in memory at a time.
# total = 0
# count = 0
# while True :
#     inp = input('Enter a Number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total += value
#     count += 1
# average = total / count
# print('Average:', average)

# New way to do it. Uses more memory. Requires an extra bit for each number.
print("Hi! I'd like to get you an average on a set of numbers.")
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp.lower() == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Here are all inputs:', (numlist[:]))
print('Here is the average:', average)