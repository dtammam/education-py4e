number = 0
total = 0.0

while True :
    string_value = (input('Please enter a number: '))
    if string_value == 'done'.lower() :
        break

    float_value = float(string_value)
    print (float_value)
    number = number + 1
    total = total + float_value

print('Finished!')