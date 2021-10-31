'''
Looping and Counting

    - We can selectively count certain elements as we loop
    - In this example, we only want to know how many letter 'a' exist in the word
'''
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)