'''
XML Schema
    - Description of the legal format of an XML document
    - Expressed in terms of constraints on the structure and content of documents
    - Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema."
    - If a particular piece of XML meets the specification of the Schema - it is said to "validate"
'''
# XML Document

# <person>
#     <lastname>Severance</lastname>
#     <age>17</age>
#     <dateborn>2001-04-17</dateborn>
# </person>

# XML Schema Contract

# <xs:complexType name="person">
#     <xs:sequence>
#         <xs:element name="lastname" type="xs:string"/>
#         <xs:element name="age" type="xs:integer"/>
#         <xs:element name="dateborn" type="xs:date"/>
#     </xs:sequence>
# </xs:complexType>