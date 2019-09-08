from random import randint
from PIL import Image

length = 3 #Expected length for each mon
fileName = "paintingMons.txt" #Files that hold all the info about the mons

class mon(object):
 def __init__(self, red, green, blue):
     self.red = red
     self.green = green
     self.blue = blue

pool = []

def importMons(fileName):
    monsArray = []
    with open(fileName, "r") as f:#This entire statement imports the mons from the file and ignores invalid mons and comments(denoted with a # at the start only)
        fileContent = f.readlines()
        for i in range(len(fileContent)):
            line = (fileContent[i].strip("\n")).split(",")
            if line[0][0] == "#":continue
            if(len(line) == length):
                #Add that mon to the array of mons
                for j in range(length):
                    line[j] = int(line[j])
                monsArray.append(mon(*line))
            else:
                print("Line ",i+1, " is invalid")
    return monsArray

def writeMon(monData):
    with open(fileName, "a") as f:
        f.write(",".join(monData) + "\n")


#Creating mons -----------------------------------------

def getParents():
    p1,p2 = randint(0,len(pool)-1),randint(0,len(pool)-1)
    while p1 == p2:#Gets rid of any duplicates. We can't have any babies being born out of 1 person
        p2 = randint(0,len(pool))

    return [pool[p1],pool[p2]]

def createChild():
    parents = getParents()

    childData = [
        parents[randint(0,1)].red,
        parents[randint(0,1)].green,
        parents[randint(0,1)].blue,
    ]
    writeMon(childData)
    return mon(*childData)

def createChildren(numOfChildren):
    for i in range(numOfChildren):
        pool.append(createChild())


#Main Program starts ----------------------------
pool = importMons(fileName)

