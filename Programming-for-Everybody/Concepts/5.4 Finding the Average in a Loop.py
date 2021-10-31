'''
Finding the Average in a Loop

    - Averaging is simply dividing the sum of numbers by the total number of numbers included
    - We represent this with multuple variables - sum, count and value
'''
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)