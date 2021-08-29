'''
String Comparison
    - < and > work for letters
    - Z is < than a
'''

word = input('Please input a word:')

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')