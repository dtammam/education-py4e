'''
Function Parameters

    - Function parameters allow us to sub in values for functions
    - They are very useful and are the 'backend' operators for functions
'''
def greet(lang) :
    if lang == 'es':
        print ('Hola!')
    elif lang == 'fr':
        print('Bonjour!')
    else:
        print('Hello!')

greet('es')