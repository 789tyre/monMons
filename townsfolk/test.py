from PIL import Image

fileName = "monMons.txt"
length = 3
base = Image.open("baseMon.png")
pool = []

class mon(object):
    def __init__(self, color):
        self.color = color # As a integer tupple of 3 numbers

        
def importMons(fileName):
    monsArray = []
    with open(fileName, 'r') as f:
        fileContent = f.readlines()
        for i in range(len(fileContent)):
            line = (fileContent[i].strip("\n")).split(",") # splits the line into the core components
            if line[0][0] == "#": continue #ignores comments (denoted by "#" at the start)

            if(len(line) == length):
                monsArray.append(mon((int(line[0]), int(line[1]), int(line[2]) )))
            else:
                print("Line ", i+1, " is invalid")
    return monsArray

def writeMon(monData):
    strMonData = []
    for i in range(len(monData)):
        strMonData.append(str(monData[i]))
    
    
    with open(fileName, "a") as f:
        f.write(",".join(strMonData) + "\n")

#Let's create some monMons! ---------------------------------------------------
def getParents():
    p1,p2 = randint(0,len(pool)-1),randint(0,len(pool)-1)
    #Gets rid of any duplicates. We can't have any babies being born out of 1 person
    while p1 == p2:
        p2 = randint(0,len(pool)-1)
 
    return [pool[p1],pool[p2]]
 
def createChild():
    parents = getParents()
 
    childData = [
        parents[randint(0,1)].color[0],
        parents[randint(0,1)].color[1],
        parents[randint(0,1)].color[2],
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
# Let's create some townsfolk! ------------------------------------------------
def paintMon(mon):
    img = Image.open("baseMon.png")
    for y in range(img.height):
        for x in range(img.width):
            if img.getpixel((x, y)) == (0,0,0):
                img.putpixel((x, y), (mon.color[0], mon.color[1], mon.color[2]))
    return img

#Main program start -----------------------------------------------------------
pool = importMons(fileName)

for i in range(len(pool)):
    paintMon(pool[i]).save("images/{}.png".format(i))

