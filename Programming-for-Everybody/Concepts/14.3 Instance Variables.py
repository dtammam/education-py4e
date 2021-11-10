'''
Instance Variables

    - Constructors can have additional parameters.
    - These can be used to set up instance variables for the particular instance of the class (i.e., for the particular object).
    - We have two independent instances.
'''
class PartyAnimal:
    x = 0
    # Defining an instance method
    name = ""
    # Referencing the new instance variable after self for the specific instance
    def __init__(self, z):
        # Using it as a method and defining the variable within this class
        self.name = z
        # Call the method and announce that its' been constructed
        print(self.name,"constructed")

    def party(self):
        self.x += 1
        # Print the name and count how many times its' been called
        print(self.name,"party count",self.x)

# Define Sally as a name using as a parameter of the class
s = PartyAnimal("Sally")
s.party()

# Define Jim as a name using as a parameter of the class
j = PartyAnimal("Jim")
j.party()
s.party()