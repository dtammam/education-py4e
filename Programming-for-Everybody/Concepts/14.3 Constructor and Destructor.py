'''
Constructor and Destructor

	- Objects are created, used and discarded
	- We have special blocks of code (methods) that get called
	    - At the moment of creation (constructor)
		- At the moment of destruction (destructor)
	- Constructors are used a lot
    - Destructors are seldom used and happen organically when overwriting variables or when a program closes
'''
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed!')
    
    def party(self):
        self.x += 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed with my last value having been', self.x)

an = PartyAnimal()
an.party()
an.party()
# Before we throw away the value of an, the object notices something
# It notices we've written a registered destructor... process this
an = 42
print('an contains',an)