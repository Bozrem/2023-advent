import re

class Set:
    def __init__(self, reds, greens, blues):
        self.reds = reds
        self.greens = greens
        self.blues = blues
    
    def isSetGreaterThanCriteria(self, maxSet): # Going wrong here
        if (self.reds > maxSet.reds or self.greens > maxSet.greens or self.blues > maxSet.blues):
                return True # Does not fit criteria
        return False # Fits criteria
    
    def __str__(self) -> str:
        return (f"{self.reds} reds, {self.greens} greens, {self.blues} blues")
    
    def getPower(self) -> int:
        return self.reds * self.greens * self.blues

class Game:
    sets: list[Set]
    id: int

    def __init__(self, id: int):
        self.sets: list[Set] = []
        self.id = id

    def addSet(self, newSet: Set):
        self.sets.append(newSet)

    def isPossible(self, maxSet: Set) -> bool:
        for set in self.sets:
            if (set.isSetGreaterThanCriteria(maxSet)):
                return False # Not possible: it has one greater than max
        return True # Possible
    
    def getMinimumPossibleSet(self) -> Set:
        maxReds = 0
        maxGreens = 0
        maxBlues = 0

        for set in self.sets:
            maxReds = max(maxReds, set.reds)
            maxGreens = max(maxGreens, set.greens)
            maxBlues = max(maxBlues, set.blues)

        return Set(maxReds, maxGreens, maxBlues)
    
    def __str__(self) -> str:
        string: str = f"Game {self.id}: "
        for set in self.sets:
            string += (f"{set}; ")
        return string
    

def extractGameFromLine(line: str) -> Game:
    gameParts = line.split(": ")
    gameAndID = gameParts[0]
    gameSetData = gameParts[1]

    gameFromLine = Game(int(re.findall(r'\d+', gameAndID)[0]))

    sets = gameSetData.split("; ")

    for set in sets:
        setObject: Set = Set(0, 0, 0)
        colors = set.split(", ")
        for color in colors:
            if color.__contains__("red"):
                setObject.reds = int(re.findall(r'\d+', color)[0])
            if color.__contains__("green"):
                setObject.greens = int(re.findall(r'\d+', color)[0])
            if color.__contains__("blue"):
                setObject.blues = int(re.findall(r'\d+', color)[0])
        gameFromLine.addSet(setObject)
    
    return gameFromLine

# Part 1
maxSet = Set(12, 13, 14)
extractedGames : list[Game] = [] 
total: int = 0
with open('day-two/Advent2023DayTwoInput.txt', 'r') as file:
    for line in file:
        line = line.strip()
        extractedGames.append(extractGameFromLine(line))

for game in extractedGames:
    if (game.isPossible(maxSet)):
        total += game.id

print(f"Sum of possible games IDs = {total}")

# Part 2
totalPower: int = 0
for game in extractedGames:
    totalPower += game.getMinimumPossibleSet().getPower()

print(f"Total power from all games: {totalPower}")
    