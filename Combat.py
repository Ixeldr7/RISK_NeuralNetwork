from Territory import Territory
from random import randint

class Combat():
    #function for combat
    def combat(attacking, defending):
        attacking.printDetails()
        defending.printDetails()
        a = attacking.getUnits()
        b = defending.getUnits()
        print(a)
        print(b)

        combat = 1
        while combat == 1:
            rollA = randint(1,6)
            print("Attacking roll = " + str(rollA))
            #roll is made for the defenders
            rollB = randint(1,6)
            print("Defending roll = " + str(rollB))
        
            #if the attackers rol higher than the defenders
            if rollA > rollB:
                #the defenders lose a unit
                b = b - 1
                print("The defenders have lost a unit")
            #else the attackers lose a unit
            if rollB >= rollA:
                a = a - 1
                print("The attackers have lost a unit")
            #checks resolve conditions at the end of each combat iteration
            if a == 0:
                print("The attacking force was defeated")
                attacking.setUnits(1)
                combat = 0
            if b == 0:
                print("The defending force was defeated")
                defending.setUnits(a)
                attacking.setUnits(1)
                x = defending.getOwner()
                x = x.strip()
                print(x)
                defending.updateOwner(x)
                combat = 0
