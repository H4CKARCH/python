class flower:

    # Common base class for all Flowers

    def __init__(self, petalName, petalNumber, petalPrice):

        self.name = petalName

        self.petals = petalNumber

        self.price = petalPrice

    def setName(self, petalName):

        self.name = petalName

    def setPetals(self, petalNumber):

        self.petals = petalNumber

    def setPrice(self, petalPrice):

        self.price = petalPrice

    def getName(self):

        return self.name

    def getPetals(self):

        return self.petals

    def getPrice(self):

        return self.price


# This would create first object of Flower
f1 = flower("jasmin", 6, 200)

print("Flower Details:")

print("Name:", f1.getName())

print("Number of petals:", f1.getPetals())

print("Price:", f1.getPrice())

print("\n")


# This would create second object of Flower
f2 = flower("lotus", 4, 100)

f2.setPrice(30)

f2.setPetals(5)

print("Flower Details:")

print("Name:", f2.getName())

print("Number of petals:", f2.getPetals())

print("Price:", f2.getPrice())


#OUTPUT

Flower Details:
Name: jasmin
Number of petals: 6
Price: 200


Flower Details:
Name: lotus
Number of petals: 5
Price: 30
