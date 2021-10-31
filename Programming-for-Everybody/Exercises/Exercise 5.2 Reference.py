largest = -1
smallest = None

while True:
    string_input = input("Enter a number: ")
    if string_input == 'done':
        break
    try:
        validinput = float(string_input)
    except:
        print('Invalid input')
        continue
    if validinput > largest:
        largest = validinput
    if smallest is None: 
        smallest = validinput
    elif validinput < smallest:
        smallest = validinput   
         
print('Maximum is', int(largest))
print('Minimum is', int(smallest))