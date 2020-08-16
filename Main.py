#import statements
import numpy as np
from Territory import Territory 
from Combat import Combat
from networkControl import neuralNetwork

#training set for the neural network
#currentTerritoryStrength, adjcentTerritory1 strength, adjacentTerritory2 strength, adjacentTerritory3 strength
trainingSet = np.array([[1,0.7,0.5,0],
    [0.8,0.5,0.6,0.2],
    [0.3,0.8,0,0],
    [0.5,0.7,0.2,0],
    [0.4,0.9,0.5,0.6],
    [0.5,0.6,0.2,0],
    [0.1,0.3,0.1,0],
    [0.2,0.3,0.3,0],
    [0.5,0.3,0.3,0],
    [0.4,0.3,0.3,0],
    [0.4,0.8,0.3,0],
    [0.1,0.3,0.1,0],
    [0.1,0.3,0.1,0],
    [0.4,0.3,0.3,0],
    [0.1,0.5,0.3,0],
    [0.3,0.3,0.3,0],
    [0.1,0.3,0.1,0],
    [0.4,0.3,0.3,0],
    [0.1,0.3,0.1,0],
    [0.3,0.1,0.1,0],
    [0.4,0.3,0.3,0],
    [0.1,0.3,0.1,0],
    [1,0.7,0.5,0],
    [0.1,0.3,0.1,0],
    [0.4,0.3,0.3,0],
    [0.4,0.3,0.3,0],
    [0.1,0.3,0.1,0],
    [0.3,0.8,0,0],
    [0.3,0.3,0.3,0],
    [0.3,0.3,0.3,0],
    [0.3,0.1,0.1,0],
    [0.1,0.3,0.1,0],
    [0.4,0.9,0.5,0.6],
    [0.3,0.3,0.3,0]])

#opens the training set file for reading
#trainingFile = open("TrainingSet.txt", "r")
#readData = trainingFile.readlines()
#trainingSet = np.array(list(readData))
#print(str(trainingSet))

#desired Output for the neural network
desiredOutput = np.array([[0.1,0.3,0.5,0],
    [0.2,0.5,0.4,0.8],
    [0.7,0.2,0,0],
    [0.5,0.3,0.8,0],
    [0.6,0.1,0.5,0.4],
    [0.5,0.4,0.8,0],
    [0.9,0.7,0.9,0],
    [0.8,0.7,0.7,0],
    [0.5,0.7,0.7,0],
    [0.6,0.7,0.7,0],
    [0.6,0.2,0.7,0],
    [0.9,0.7,0.9,0],
    [0.9,0.7,0.9,0],
    [0.6,0.7,0.7,0],
    [0.9,0.5,0.7,0],
    [0.7,0.7,0.7,0],
    [0.9,0.7,0.9,0],
    [0.6,0.7,0.7,0],
    [0.9,0.7,0.9,0],
    [0.7,0.9,0.9,0],
    [0.6,0.7,0.7,0],
    [0.9,0.7,0.9,0],
    [0.1,0.3,0.5,0],
    [0.9,0.7,0.9,0],
    [0.6,0.7,0.7,0],
    [0.6,0.7,0.7,0],
    [0.9,0.7,0.9,0],
    [0.7,0.2,0,0],
    [0.7,0.7,0.7,0],
    [0.7,0.7,0.7,0],
    [0.7,0.9,0.9,0],
    [0.9,0.7,0.9,0],
    [0.6,0.1,0.5,0.4],
    [0.7,0.7,0.7,0]])

#initialise main variables
game = 1
dataFiles = []
Player = ["A", "B"]
player = 0
currentPlayer = " "
Owner = []
Territories = []
adjacentTerritory = []

def appendTrainingSet(data, output):
    #opens the training set file for writing
    trainingFile = open("TrainingSet.txt", "w")

    #prepares training set for writing
    newTrainingSet = np.append(trainingSet, data)
    newTrainingSet = str(newTrainingSet)
    trainingFile.write(newTrainingSet)
    trainingFile.close()
    
    #np.savetxt("TrainingSet.txt", newTrainingSet, "", )
    
    newDesiredOutput = np.append(desiredOutput, output)

def assignData():
    dataFiles.append("North America.txt")
    dataFiles.append("South America.txt")
    dataFiles.append("Africa.txt")
    dataFiles.append("Europe.txt")
    dataFiles.append("Asia.txt")
    dataFiles.append("Oceania.txt")

def createTerritories():
    i = 0
    while i < 6:
        dataFile = open(dataFiles[i], "r")
        #creates a new object of type Territory
        name = dataFile.readline()
        owner = dataFile.readline()
        units = int(dataFile.readline())
        adjacent_territory1 = dataFile.readline()
        adjacent_territory2 = dataFile.readline()
        adjacent_territory3 = dataFile.readline()
        territory = Territory(name,owner,units,adjacent_territory1,
                              adjacent_territory2,adjacent_territory3)

        Territories.append(territory)
        
        i = i + 1
    
def printAllDetails():
    i = 0
    while i < 6:
        Territories[i].printDetails()
        i = i + 1

def printOwnedTerritories(current):
    i = 0
    print("## TERRITORIES OWNED BY PLAYER " + current + " ##")
    while i < 6:
        ownerCheck = Territories[i].getOwner()
        ownerCheck = ownerCheck.strip()
        if ownerCheck == current:
            Territories[i].printDetails()
        i = i + 1
    print("## TERRITORIES OWNED BY PLAYER " + current + " ##")

def printEnemyTerritories(current):
    i = 0
    print("## TERRITORIES OWNED BY YOUR OPPONNENT ##")
    while i < 6:
        ownerCheck = Territories[i].getOwner()
        ownerCheck = ownerCheck.strip()
        if ownerCheck != current:
            Territories[i].printDetails()
        i = i + 1
    print("## TERRITORIES OWNED BY YOUR OPPONNENT ##")
    
def reinforcement(current):
    inputText = 1
    i = 0
    printOwnedTerritories(current)
    current = current.strip()
    while inputText == 1:
        territory = input("Choose one of the above territories to reinforce")
        #checks the user entered an integer
        if territory.isdigit():
            territory = int(territory)
            #checks that the user has chosen a valid integer
            if(territory > 5):
                print("Please choose a valid territory")
            else:
                check = Territories[territory].getOwner()
                check = check.strip()
        
                if(check == current):
                    Territories[territory].reinforceUnits(3)
                    inputText = 0
                else:
                    print("Please choose a territory you control")
        else:
            print("You must enter an integer")
            

def getAdjacentTerritories(attacking):
    adjacentTerritory.append(Territories[attacking].getAdjacentTerritory1())
    adjacentTerritory.append(Territories[attacking].getAdjacentTerritory2())
    adjacentTerritory.append(Territories[attacking].getAdjacentTerritory3())
    for x in range(0,2):
        print(adjacentTerritory[x])
        Territories[x].printDetails()

#if all territories are owned by own player, the game ends        
def checkVictory(game,current):
    i = 0
    while i < 6:
        Owner.append(Territories[i].getOwner())
        i += 1
    #converts Owner to a set, a set cannot have duplicates
    #if every element is identical it will return 1
    if len(set(Owner)) == 1:
        #this means all territories are owned by one player
        game = 0
        return game
    else:
        game = 1
        return game

    
def getPlayer(player):
    if(player == 0):
        return "A"
    if(player == 1):
        return "B"

def playerTurn(currentPlayer):
    attackingCheck = 1
    defendingCheck = 1
    #user selects a territory for each stage
    print("########### FULL GAME DETAILS ###########")
    printAllDetails()
    print("########### FULL GAME DETAILS ###########")
    #reinforcement
    reinforcement(currentPlayer)
    #combat
    while attackingCheck == 1:
        attacking = input("Choose a territory above to attack from")
        #checks user input
        if attacking.isdigit():
            attacking = int(attacking)
            if attacking > 5:
                print("Please choose a valid territory")
            else:
                check = Territories[attacking].getOwner()
                check = check.strip()
                if(check == currentPlayer):
                    attackingCheck = 0
                else:
                    print("Choose a territory you control")
        else:
            print("You must enter an integer")
            
    #getAdjacentTerritories(attacking)
    printEnemyTerritories(currentPlayer)
    while defendingCheck == 1:
        defending = input("Choose one of the above territories to attack")
        #checks user input
        if defending.isdigit():
            defending = int(defending)
            if defending > 5:
                print("Please choose a valid territory")
            else:
                check = Territories[defending].getOwner()
                check = check.strip()
                if(check != currentPlayer):
                    defendingCheck = 0
                else:
                    print("Choose a territory your opponent controls")
        else:
            print("You must enter an integer")

    #runs the combat algorithm
    attacking = Territories[attacking]
    defending = Territories[defending]
    Combat.combat(attacking,defending)

#converts game data in to a format to be processed by the neural network
def prepData(i):
    currentTerritory = Territories[i]
    x1 = 0.0 + (currentTerritory.getUnits() / 10)
    
    x2 = int(currentTerritory.getAdjacentTerritory1())
    x2 = 0.0 + (Territories[x2].getUnits() / 10)
    
    x3 = currentTerritory.getAdjacentTerritory2()
    if(x3 is not None):
        x3 = 0.0 
    else:
        x3 = 0.0 + (Territories[int(x3)].getUnits() / 10)
        
    x4 = currentTerritory.getAdjacentTerritory3()
    if(x4 is not None):
        x4 = 0.0
    else:
        x4 = 0.0 + (Territories[int(x4)].getUnits() / 10)

    values = np.array([[x1, x2, x3, x4]])
    return values

def findMaxValue(output):
    maximum = 0.0
    index = 0
    for y in range(4):
        x = output[0,y]
        if(x > maximum):
            maximum = x
            index = y
    #print("The maximum value is at index " + str(index) + " with a value of " + str(maximum))
    return maximum, index

#reinforce the friendly territory with the highest value identified by the neural network
def computerReinforce(currentPlayer, indexList, valueList):
    territory = 0
    count = 0.0
    countIndex = 0
    position = 0
    positionList = [0,1,2,3,4,5]
    i = 0
    while i < 6:
        x = valueList[i]
        y = indexList[i]
        a = Territories[i].getOwner()
        a = a.strip()
        if(count < x and a == currentPlayer):
            count = x
            countIndex = y
            position = i
        i += 1
        
    if(countIndex == 0):
        territory = Territories[position]
        territory.reinforceUnits(3)

    if(countIndex == 1):
        territory = int(Territories[position].getAdjacentTerritory1())
        Territories[territory].reinforceUnits(3)
        territory = Territories[territory]

    if(countIndex == 2):
        territory = int(Territories[position].getAdjacentTerritory2())
        Territories[territory].reinforceUnits(3)
        territory = Territories[territory]

    if(countIndex == 3):
        territory = int(Territories[position].getAdjacentTerritory3())
        Territories[territory].reinforceUnits(3)
        territory = Territories[territory]

    print("The AI reinforced " + str(territory.printDetails()))
    return territory

#attack the enemy territory with the highest value identified by the neural network
def computerAttack(currentPlayer, indexList, valueList):
    target = 0
    count = 0.0
    countIndex = 0
    position = 0
    positionList = [0,1,2,3,4,5]
    i = 0
    while i < 6:
        x = valueList[i]
        y = indexList[i]
        a = Territories[i].getOwner()
        a = a.strip()
        if(count < x and a is not currentPlayer):
            count = x
            countIndex = y
            position = i
        i += 1
        
    if(countIndex == 0):
        target = Territories[position]
        #print("Territory " + str(target))

    if(countIndex == 1):
        target = int(Territories[position].getAdjacentTerritory1())
        target = Territories[target]

    if(countIndex == 2):
        target = int(Territories[position].getAdjacentTerritory2())
        target = Territories[target]

    if(countIndex == 3):
        target = int(Territories[position].getAdjacentTerritory3())
        target = target[target]

    print("The territory to attack is " + str(target.printDetails()))
    return target

#the computers turn is controlled by the neural network
def computerTurn(currentPlayer, network):
    #loops through each territory
    i = 0
    indexList = []
    valueList = []
    while i < 6:
        #data is prepared
        data = prepData(i)
        #the neural network processes this data
        output = network.useNetwork(data)
        #appendTrainingSet(data, output)
        #print(str(output))
        #finds the highest value returned by the neural network
        maximum, index = findMaxValue(output)
        indexList.append(index)
        valueList.append(maximum)
        i += 1
    territory = computerReinforce(currentPlayer, indexList, valueList)
    target = computerAttack(currentPlayer, indexList, valueList)
    #print("attacking " + str(territory))
    #print("defending " + str(target))
    Combat.combat(territory,target)

    
############################################
##########train the neural network##########
############################################
    
network = neuralNetwork()
for x in range(1000):
    #print("Input: \n" + str(trainingSet))
    #print("Desired Output: \n" + str(desiredOutput))
    #print("Network Output: \n" + str(network.feedForward(trainingSet)))
    #print("\n")
    network.trainNetwork(trainingSet, desiredOutput)
    
print("Network has been prepared")

############################################
##########train the neural network##########
############################################

assignData()
createTerritories()
while game == 1:
    #player is initially zero
    player = 0
    currentPlayer = getPlayer(player)
    print("Player " + currentPlayer + " - It is your turn")
    playerTurn(currentPlayer)
    player = 1
    currentPlayer = getPlayer(player)
    print("AI " + currentPlayer + " - It is your turn")
    computerTurn(currentPlayer, network)
    #prints details post combat
    printAllDetails()
    game = checkVictory(game, currentPlayer)
    
    
