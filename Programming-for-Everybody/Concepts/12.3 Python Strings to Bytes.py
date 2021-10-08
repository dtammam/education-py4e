'''
Python Strings to Bytes
    - When we talk to an external resource like a network socket we send bytes, so we need to encode Python 3 strings into a given character encoding
    - When we read data from external resource, we must decode it based on the character set so that its' properly represented in Python 3 as a string
'''

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# Bytes properly encoded in UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# Sending the bytes out with cmd
mysock.send(cmd)

while True:
    # Bytes
    data = mysock.recv(512)
    if ( len(data) < 1 ) : 
        break
    # Unicode
    mystring = data.decode()
    print(mystring)