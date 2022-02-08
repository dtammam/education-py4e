'''
Collatz Conjecture

- The goal of this script is to functionally execute the idea behind the Collatz Conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)
- Prompts the user for a number to test and counts the operations taken to get to 1.
- Very simple execution of the idea. Not using a function, likely could for efficiencies' sake.
- Last thing to do is to sanitize inputs to accept only numbers (will do in the near future).
'''

prompt = int(input("Please input a number: "))
number = prompt
count = 0 

print("The original number is", number)

while True:
    if number == 1:
        break

    elif number % 2 == 0:
        print(number, 'is even, continuing.')
        number = int(number / 2)
        print('Number is now', number)
        count += 1
        continue
    
    elif number % 2 != 0:
        print(number, 'is odd, continuing.')
        number = int((number * 3) + 1)
        print('Number is now', number)
        count += 1
        continue

print('It took', count, 'operations to get to 1!')