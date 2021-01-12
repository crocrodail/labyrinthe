direction = "est"
def convert_to_bidimensionnel(target):
    structure = {}
    for line in target.read().split('\n'):
        structure[len(structure)] = list(line)
    return structure

def convert_to_text(table):
    result = ""
    for value in table:
        for v in table[value]:
            result = result + v
        result = result + "\n"
    return result

def getLymb(file):
    with open(file, mode="r") as target:
        return convert_to_bidimensionnel(target)

def plusCourtChemin(station1, station2):
    Lymbirinth = getLymb('entrer.txt')
    actualPosition = station1
    move = 0
    def front():
        global direction
        newPosition = []
        if direction == "north":
            newPosition = [actualPosition[0]-1, actualPosition[1]]
        elif direction == "south":
            newPosition = [actualPosition[0]+1, actualPosition[1]]
        elif direction == "ouest":
            newPosition = [actualPosition[0], actualPosition[1]-1]
        elif direction == "est":
            newPosition = [actualPosition[0], actualPosition[1]+1]
        return newPosition

    def changeDirection():
        global direction
        if direction == "est":
            direction = "north"
        elif direction == "north":
            direction = "ouest"
        elif direction == "ouest":
            direction = "south"
        elif direction == "south":
            direction = "est"

    def canForward():
        if Lymbirinth[front()[0]][front()[1]] != "#":
            return True
        else:
            return False

    def canGoRight():
        global direction
        newPosition = []
        d = "est"
        if direction == "est":
            d = "south"
        elif direction == "north":
            d = "est"
        elif direction == "ouest":
            d = "north"
        elif direction == "south":
            d = "ouest"
        if d == "north":
            newPosition = [actualPosition[0]-1, actualPosition[1]]
        elif d == "south":
            newPosition = [actualPosition[0]+1, actualPosition[1]]
        elif d == "ouest":
            newPosition = [actualPosition[0], actualPosition[1]-1]
        elif d == "est":
            newPosition = [actualPosition[0], actualPosition[1]+1]
        if Lymbirinth[newPosition[0]][newPosition[1]] != "#":
            return True
        else:
            return False

    def turnRight():
        global direction
        if direction == "est":
            direction = "south"
        elif direction == "north":
            direction = "est"
        elif direction == "ouest":
            direction = "north"
        elif direction == "south":
            direction = "ouest"

    def forward():
        if canForward() and not canGoRight():
            return front()
        elif canGoRight():
            turnRight()
            return front()
        else:
            changeDirection()
            return forward()

    while actualPosition != station2:
        nextStep = forward()
        Lymbirinth[nextStep[0]][nextStep[1]] = "."
        actualPosition = [nextStep[0], nextStep[1]]
        move = move + 1
    print("Lymbirinth résolu en "+str(move)+" action, resultat:\n")
    print(convert_to_text(Lymbirinth))



                #axe X,   axe Y
plusCourtChemin([15, 1], [5, 16])
