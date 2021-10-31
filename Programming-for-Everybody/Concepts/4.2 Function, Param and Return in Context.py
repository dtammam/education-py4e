'''
Function, Param and Return in Context

    - You can see a proper example of all elements below
    - Note the printing of greet(), we need to call it for it to run
'''

def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    else :
        return 'Hello'

print(greet('es'), 'Glenn')
print(greet('en'), 'Sally')
print(greet('fr'), 'Michael')