'''
Our First Class and Object

	- class is a reserved word.
	- This is the template for making PartyAnimal objects.
	- Each PartyAnimal object has a bit of data.
	- Each PartyAnimal object has a bit of code.
	- Construct a PartyAnimal object and store in the 'an' variable.
	- Tell the 'an' object to run the party() code within it.
    - Equivalent to PartyAnimal.party(an)
'''
# This is the template for making PartyAnimal objects.
class PartyAnimal:

    # Each PartyAnimal object has a bit of data.
    x = 0

    # Each PartyAnimal object has a bit of code.
    def party(self):
        self.x += 1
        print("So far",self.x)

# Construct a PartyAnimal object and store in the 'an' variable
# The moment of construction
an = PartyAnimal()

# Tell the 'an' object to run the party() code within it
# Invoking the method within the object
an.party()
an.party()
an.party()
# Interchangeable with PartyAnimal.party(an) 
# It boils down to 'Go into PartyAnimal, call the Party function within that and then pass this variable as the first parameter
PartyAnimal.party(an)

# We can use dir() to find the "capabilities" of our newly created class
print("Type", type(an))
print("Dir", dir(an))