'''
Breaking Out of a Loop

    - The break command allows us to deliberately stop looping
    - This is useful if we get the result we want and no longer need to continue
'''
print("What is the magic word?")

while True:

    line = input('> ').lower()
    
    if line == 'now' :
        print ('Wow, that was rude.')

    elif line == 'please' :
        break
    
    print('Magic word not accepted. Try again, please.')
    
print('Magic word accepted!')