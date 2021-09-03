bottles = 99

while bottles > 1 :
    print(bottles, 'bottles of beer on the wall,', bottles, 'bottles of beer...')
    bottles -= 1
    print('You take one down and pass it around,', bottles, 'bottles of beer on the wall!\n')
        
while bottles == 1 :
    print('Only', bottles, 'bottle of beer on the wall, only', bottles, 'bottles of beer...')
    bottles -= 1
    print("You take it down and pass it around, and now theres no bottles of beer on the wall!")