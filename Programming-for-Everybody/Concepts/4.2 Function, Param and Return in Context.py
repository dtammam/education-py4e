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