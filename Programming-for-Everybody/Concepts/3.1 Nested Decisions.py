'''
Nested Decisions

    - Decisions can be made at multiple levels of loops
    - In this example, we are checking for multiple conditions and can interact accordingly
'''
w = input("What is our reference number?")
x = int(w)

if x > 1 :
    print('Our number is most certainly larger than 1. Huzzah!')
    if x < 100:
        print('Our number is also less than 100. Cheerio!')
print('I am now bored. Our reference subject is now free to go off into the world, to be the number it was always meant to be.')