from random import randint

pool = []

def importMons(fileName, length):

    try:
        test = mon(*range(length))
    except NameError:
        print("The monMons are nonexistant in this file")
        return []

    monsArray = []
    with open(fileName, "r") as f:
        fileContent = f.readlines()
        print(fileContents)

        for i in range(len(fileContent)):
            print("hi")
            line = (fileContent[i].strip("\n")).split(",")

            if(len(line) == length):
                monsArray.append(mon(*line))
            else:
                print("Line ", i + 1, " is invalid")

    return monsArray

#Let's create some monMons! ---------------------------------------------------
def getParents():
    p1, p2 = randint(0, len(pool) - 1 ), randint(0, len(pool) - 1 )

    while p1 == p2:
        p2 = randint(0, len(pool - 1))
    
    return [p1, p2]

def createChildren(numOfChildren):
    try:
        newMons = []
        for i in range(numOfChildren):
            newMons.append(createChild)
    except NameError:
        print("How to create children when you have no way to make any!?")
    return newMons
