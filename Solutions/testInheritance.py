class Structure:
    def __init__(self, _type, sqfoot):
        self._type = _type
        self.sqfoot = sqfoot

    def info(self):
        print("Type: " + self._type + "\nSquare Feet: " + str(self.sqfoot))


class House(Structure):
    def __init__(self, _type, sqfoot, rooms, bath):
        super(House, self).__init__(_type, sqfoot)
        self.rooms = rooms
        self.bath = bath

    def info(self):
        super(House, self).info()
        print("Bedrooms: " + str(self.rooms) + "\nBatrooms: " + str(self.bath))

class Barn(Structure):
    def __init__(self, _type, sqfoot, stables):
        super(Barn, self).__init__(_type, sqfoot)
        self.stables = stables

    def info(self):
        super(Barn, self).info()
        print("Stables: " + str(self.stables))
        

h = House("Split Level", 1200, 3, 2.5)
b = Barn("Farm Barn", 2000, 8)
p = Structure("Pavillion", 1500)

structures = [h,b,p]

for s in structures:
    s.info()
    print("----------")
