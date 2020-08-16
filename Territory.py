
class Territory(object):
    def __init__(self,name,owner,units, adjacent_territory1,
                 adjacent_territory2, adjacent_territory3):
        self.name = name
        self.owner = owner
        self.units = units
        self.adjacent_territory1 = adjacent_territory1
        self.adjacent_territory2 = adjacent_territory2
        self.adjacent_territory3 = adjacent_territory3
        
    #territory functions
        
    #changes the territory owner
    def updateOwner(self,x):
        if x == "A":
            self.owner = "B"
            print(self.owner)
        else:
            self.owner = "A"
            print(self.owner)

    #getter methods
            
    def getOwner(self):
        y = self.owner
        return y

    def getAdjacentTerritory1(self):
        y = self.adjacent_territory1
        return y

    def getAdjacentTerritory2(self):
        y = self.adjacent_territory2
        return y

    def getAdjacentTerritory3(self):
        y = self.adjacent_territory3
        if(y is None):
            #print("y is none")
            y = 0
        return y
        
        
    #updates the number of units in the territory
    def reinforceUnits(self, units):
        self.units = self.units + units
        self.printDetails()

    def getUnits(self):
        x = self.units
        return x

    def setUnits(self,units):
        self.units = units
        
    #prints the territory details
    def printDetails(self):
        print(self.name + " " + "contains " + str(self.units) + " units "
              + "and is owned by player: " + self.owner)
