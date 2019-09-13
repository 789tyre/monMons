from random import randint
from PIL import Image
from math import floor

length = 6
fileName = "mons.txt"
rangeOfStats = 255
chanceOfMutation = 4

pool = []

class mon(object):
    def __init__(self, health, attack, defence, red, green, blue):
        self.health = int(health)
        self.fullHealth = int(health)
        self.attack = int(attack)
        self.defence = int(defence)
        self.wins = 0
        self.lives = 3
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)

    def Attack(self):
        chance = randint(1, rangeOfStats)
        if chance <= self.attack:
            return chance
        else:
            return 0

    def Defend(self):
        chance = randint(1, rangeOfStats)
        if chance <= self.defence:
            return chance
        else:
            return 0

def importMons(fileName):
    mons = []
   #Imports all the mons and creates an instance for each of them
    with open(fileName, "r") as f:
        filecontent = f.readlines()
        for i in range(len(filecontent)):
            line = (filecontent[i].strip("\n")).split(",")
            if line[0][0] == "#": continue
            if(len(line) == length):
                #Proceed to add that mon to the pool
                mons.append(mon(*line))
            else:
                print("Line ", i+1, " is invalid")

    return mons

def writeMon(monData):
    for i in range(len(monData)):
        monData[i] = str(monData[i])
    with open(fileName, "a") as f:
        monData = ",".join(monData); monData += "\n"
        f.write(monData)

#Let's create some monMons!----------------------------------------------------
def getParents():
    p1, p2 = randint(0, len(pool)-1), randint(0, len(pool)-1)
    while p1 == p2:
        p2 = randint(0, len(pool)-1)
    return [pool[p1], pool[p2]]

def createChild():
    #Creates 1 child and mutates it by chance
    #Then it returns the child
    parents = getParents()

    childData = [
                parents[randint(0,1)].health,
                parents[randint(0,1)].attack,
                parents[randint(0,1)].defence,
                parents[randint(0,1)].red,
                parents[randint(0,1)].green,
                parents[randint(0,1)].health,
            ]
    for i in range(length):
        chance = randint(1, chanceOfMutation)
        if chance == 1:
            chance = randint(-2,2)
            childData[i] += chance

    writeMon(childData)
    return mon(*childData)

def createChildren(numOfChildren):
    #Used to create a large amount of children but does not write it to the file
    #It returns all the children it created 
    newMons = []
    for i in range(numOfChildren):
        newMons.append(createChild())
    return newMons
#This is where all the monMons go to fight ------------------------------------

def clash(mon1, mon2):
    #This deals with the damage calulation and updating health values
    mon1turn = mon1.Attack()
    mon2turn = mon2.Defend()
    damage = mon1turn - mon2turn
    damage = damage if (damage > 0) else 0
    mon2.health -= damage

def fight(mon1, mon2):
    #This is where the winner of the 2 monMons is decided
    while mon1.health > 0 and mon2.health > 0:
        clash(mon1, mon2)
        if (mon2.health <= 0): return [mon1, mon2]
        clash(mon2, mon1)

    if(mon1.health <=0):
        return[mon2, mon1]
    else:
        return [mon1, mon2]

def startBattleRoyale(winnersLeft):
    #This is where 2 monMons are randomly selected and pitted against each other
    #Until there is only 1 left
    if winnersLeft <= 0:
        return ['n','o']

    losers= []
    while True:
        results = fight(*getParents())

        pool.remove(results[1])
        results[1].lives -= 1
        if results[1].lives <=0:
            losers.append(results[1])
        else:
            results[1].health = results[1].fullHealth
            pool.append(results[1])

        if len(pool) == winnersLeft: break

        pool.remove(results[0])

        results[0].health = results[0].fullHealth
        results[0].wins += 1
        pool.append(results[0])
        print(str(len(pool)), end="\r")

    return losers

def createNewGen():
   startBattleRoyale(floor(len(pool)/2))
   with open(fileName, "w") as f:
       f.write("")
   return createChildren((255*255) - len(pool))


#Painting time for the strongest monMons --------------------------------------
def paintPool(pool):
    img = Image.new("RGB", (255,255))
    counter = 0
    for y in range(255):
        for x in range(255):
            img.putpixel((x, y), (pool[counter].red, pool[counter].green, pool[counter].blue))
            counter += 1

    img.show()
    return img

#Start of main program --------------------------------------------------------
pool = importMons(fileName)
#pool.append(createNewGen())
#paintPool(pool).save("images/1.png")
for i in range(10):
    pool += createNewGen()
    paintPool(pool).save("images1/{}.png".format(i))
