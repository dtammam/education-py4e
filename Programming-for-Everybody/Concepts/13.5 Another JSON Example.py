'''
Another JSON Example
    - Douglas Crockford 'discovered' JSON
    - Object literal notation in JavaScript
    - Looks and acts as a Python dictionary
    - Not as rich a representation of XML
    - However, it's simple and is a lot easier to use
'''

import json
example = '''
[
    {   
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"

    } ,
    {   
        "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

info = json.loads(example)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])