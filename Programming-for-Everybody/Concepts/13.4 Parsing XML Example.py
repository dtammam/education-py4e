'''
Parsing XML Example
    - We can use xml.etree.ElementTree similarly to how we used BeautifulSoup to parse XML
    - Using 'as' to create a quick attribute saves us a lot of typing later on in the code
    - This is very dependent on proper syntax. If anything is wrong with the syntax, we'll get a traceback
'''

import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone> type="intl">
        +1 734 303 4456
        </phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))