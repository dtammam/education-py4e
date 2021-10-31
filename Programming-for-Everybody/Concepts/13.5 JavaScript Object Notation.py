'''
JavaScript Object Notation

    - Douglas Crockford 'discovered' JSON
    - Object literal notation in JavaScript
    - Looks and acts as a Python dictionary
    - Not as rich a representation of XML
    - However, it's simple and is a lot easier to use
'''
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
    }'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])