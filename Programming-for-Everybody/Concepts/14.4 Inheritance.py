'''
Inheritance

    - 'Subclasses' are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own
    - FootballFan is a class which extends PartyAnimal.
    - It has all the capabilities of PartyAnimal and more.
'''
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name,"was constructed")

    def party(self):
        self.x += 1
        print(self.name,"has a party count of",self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name,"scored a touchdown, and has gained",self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()