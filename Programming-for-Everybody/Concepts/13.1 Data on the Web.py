'''
Data on the Web
    - With the HTTP Request/Response well understood and well supported, there was a natural move towards exchanging data between programs using these protocols
    - We needed to come up with an agreed way to represent data going between applications and across networks
    - There are two commonly used formats: XML and JSON

Sending Data across the Internet
    - Python Dictionary -> Internet -> Java HashMap
    - Serialize -> De-Serialize
    - Also known as "Wire Protocol", what we send on the "wire"
		
'''
# XML
#   <person>
#       <name>
#            Chuck
#       </name>
#        <phone>
#           303 4456
#         </phone>
#    </person>

# JSON
#   {
#     "name" :
#       "Chuck",
#     "phone" :
#       "303-4456"
#   }