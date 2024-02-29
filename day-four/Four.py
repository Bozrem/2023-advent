import re

def getCard(card: str):
    uselessCardSplit = card.split(':')
    parts = uselessCardSplit[1].split('|')
    # Extract extract and convert integers
    winning_numbers = [int(num) for num in re.findall(r'\d+', parts[0])]
    our_numbers = [int(num) for num in re.findall(r'\d+', parts[1])]

    return winning_numbers, our_numbers

def getCardWins(card: str):
    wins = 0
    winning, ours = getCard(card)
    ourSet = set(ours)
    for num in winning:
        if num in ourSet: wins+=1
    return wins

total = 0
with open('day-four/Advent2023DayFourInput.txt', 'r') as file:
    line = file.readline()

    while line:
        total += (int)(2 ** (getCardWins(line)-1))
        line = file.readline()

print(f"Total = {total}")