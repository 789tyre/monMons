from random import randint
from math import floor

length = 5 #Expected length for each mon
fileName = "mons.txt" #Files that hold all the info about the mons
rangeOfStats = 100 #This applies to attack and defence values
chanceOfMutation = 4 #The higher the number the less chance of mutation
pool = []

class mon(object):
    def __init__(self, name, name2, health, attack, defence):
        self.name = name
        self.name2 = name2
        self.fullHealth = health
        self.health = health
        self.attack = attack
        self.defence = defence
        self.wins = 0 # How many times did this mon win
        self.lives = 3 # Number of chances at victory
    
    def Attack(self):
        chance = randint(1, rangeOfStats)
        if chance <= self.attack:
            return chance
        else:
            return 0

    def Defend(self):
        chance = randint(1,rangeOfStats)
        if chance <= self.defence:
            return chance
        else:
            return 0


def importMons(fileName):
    #This entire statement imports the mons from the file and ignores invalid mons and comments(denoted with a # at the start only)
    with open(fileName, "r") as f:
        fileContent = f.readlines()
        for i in range(len(fileContent)):
            line = (fileContent[i].strip("\n")).split(",")
            if line[0][0] == "#":continue
            if(len(line) == length):
                #Add that mon to the array of mons
                for j in range(length-3,length):
                    line[j] = int(line[j])
                pool.append(mon(*line))
            else:
                print("Line ",i+1, " is invalid")

def writeMon(monData):
    for i in range(len(monData)):
        monData[i] = str(monData[i])
    with open(fileName, "a") as f:
        monData = ",".join(monData);monData = monData + "\n"
        f.write(monData)


#Creating new monMons function starts here -------------------------------------------

def getParents():
    p1,p2 = randint(0,len(pool)-1),randint(0,len(pool)-1)
    while p1 == p2:#Gets rid of any duplicates. We can't have any babies being born out of 1 person
        p2 = randint(0,len(pool)-1)

    return [pool[p1],pool[p2]]

def createChild():
    parents = getParents()
    #Create child here after getting what the parents are.
    childData =[
        parents[randint(0,1)].name,
        parents[randint(0,1)].name2,
        parents[randint(0,1)].health,
        parents[randint(0,1)].attack,
        parents[randint(0,1)].defence
    ]
    for i in range(2,5):
        chance = randint(1, chanceOfMutation)
        if chance == 1:
            chance = randint(-2,2)
            childData[i] += chance

    writeMon(childData)
    #pool.append(mon(*childData))
    return mon(*childData)

def createChildren(numOfChildren):
    #Can create a large amount of children from pool of monMons
    #Any new children will be added to the pool as well
    newMons = []
    for i in range(numOfChildren):
        newMons.append(createChild())
    return newMons

def createNewGen(pool):
    startBattleRoyale(floor(len(pool)/2)) #Cuts the population down
    with open(fileName, "w") as f: 
        f.write("")
    return createChildren(len(pool)*2)

# This is where the battling functions begin ------------------------------------------

def clash(mon1, mon2):
    #This deals with the damage calulation and updating the health values
    mon1turn = mon1.Attack()
    mon2turn = mon2.Defend()
    damage = mon1turn - mon2turn
    damage = damage if (damage > 0) else 0
    mon2.health -= damage

def fight(mon1, mon2):
    #This is where the winner of the two mons are decided
    while mon1.health > 0 and mon2.health > 0:
        clash(mon1, mon2)
        if (mon2.health <= 0): return [mon1, mon2]
        clash(mon2, mon1)

    if(mon1.health <= 0):
        return [mon2, mon1]
    else:
        return [mon1, mon2]
def startBattleRoyale(winnersLeft):
    #This is where 2 of the mons are randomly selected and pitted against each other.
    #Until there is only 1 left
    if winnersLeft <= 0:
        return ['n','o']
    losers = []

    while True:
        #Determine the winner
        #print(len(pool))
        results = fight(*getParents())

        #Delete the loser and the winner from the pool
        pool.remove(results[1])
        results[1].lives -= 1
        if results[1].lives <= 0:
            losers.append(results[1])
        else:
            results[1].health = results[1].fullHealth
            pool.append(results[1])
        
        if len(pool) == winnersLeft: break

        pool.remove(results[0])
        
        results[0].health = results[0].fullHealth
        #Increase the win count for the winner
        results[0].wins += 1
        #Add the updated winner back into the pool for another fight
        pool.append(results[0])

    return losers # Because the only one left in the pool will be winner

#Start of main program ----------------------------------------------------------------
importMons(fileName)
for i in range(5000):
    pool = createNewGen(pool)
print("WINNER! WINNER! WINNER!")
print("Name: {} {}".format(pool[0].name, pool[0].name2))
print("Max Health: ", pool[0].fullHealth)
print("Final Health: ", pool[0].health)
print("Attack: ", pool[0].attack)
print("Defence: ", pool[0].defence)
print("Wins: ", pool[0].wins)
print("Lives left: ", pool[0].lives)
#createChildren(5000)
