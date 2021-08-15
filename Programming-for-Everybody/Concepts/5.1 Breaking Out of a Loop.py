print("What is the magic word?")

while True:

    line = input('> ').lower()
    
    if line == 'now' :
        print ('Wow, that was rude.')

    elif line == 'please' :
        break
    
    print('Magic word not accepted. Try again, please.')
    
print('Magic word accepted!')