'''
Parsing XML Complex Example

    - In this example, the outer tag is stuff with the inner tag being users and then a user beneath that.
    - We'll write code that goes through each of the user tags with the .findall method.
    - Stuff is a tree of information that is parsed and gives us methods and attributes to use and go through the data.
'''
import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for tag in lst:
    print('Name', tag.find('name').text)
    print('Id', tag.find('id').text)
    print('Attribute', tag.get("x"))