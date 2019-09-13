from random import randint
from PIL import Image

length = 3 #Expected length for each mon
fileName = "painterMons.txt" #Files that hold all the info about the mons
rangeOfStats = 255
chanceOfMutation = 4

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
    strMonData = []
    for i in range(len(monData)):
        strMonData.append(str(monData[i]))
    
    
    with open(fileName, "a") as f:
        f.write(",".join(strMonData) + "\n")


#Creating mons ----------------------------------------------------------------

def getParents():
    p1,p2 = randint(0,len(pool)-1),randint(0,len(pool)-1)
    while p1 == p2:#Gets rid of any duplicates. We can't have any babies being born out of 1 person
        p2 = randint(0,len(pool)-1)

    return [pool[p1],pool[p2]]

def createChild():
    parents = getParents()

    childData = [
        parents[randint(0,1)].red,
        parents[randint(0,1)].green,
        parents[randint(0,1)].blue,
    ]
    
    #Mutation of the child
    for i in range(3):
        chance = randint(1,chanceOfMutation)
        if chance == 1:
            chance = randint(-2,2)
            childData[i] += chance


    writeMon(childData)
    return mon(*childData)

def createChildren(numOfChildren):
    #Creates new children for the pool
    newMons = []
    for i in range(numOfChildren):
        newMons.append(createChild())
    return newMons

#Painting functions start------------------------------------------------------
def paintPool(pool):
    img = Image.new('RGB',(64,64))
    counter = 0
    #Create an image with the Mons as the data
    for y in range(64):
        for x in range(64):
            img.putpixel((x,y), (pool[counter].red, pool[counter].green, pool[counter].blue))
            counter += 1
    return img

#Main Program starts ----------------------------------------------------------
pool = importMons(fileName)
print(len(pool))
paintPool(pool).save("img.jpg")
#createChildren(4096-len(pool))
