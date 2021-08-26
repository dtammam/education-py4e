data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

atposition = data.find('@')
print(atposition)

spaceposition = data.find(' ',atposition)
print(spaceposition)

host = data[atposition+1 : spaceposition]
print(host)