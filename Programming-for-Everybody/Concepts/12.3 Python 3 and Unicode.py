'''
Python 3 and Unicode
    - In Python 3, all strings internally are UNICODE
    - Working with string variables in Python programs and reading data from files usually "just works"
    - When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)
'''

# Byte string, different than regular string
x = b'abc'

# Regular string, different than byte string, same as unicode string
x = "平仮名"

# Unicode string, same as regular string
x = u'平仮名'