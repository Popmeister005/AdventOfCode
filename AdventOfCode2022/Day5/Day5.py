import re

puzzleInput = {}

# puzzleInput[1] = ['B','Z','T']
# puzzleInput[2] = ['V','H','T','D','N']
# puzzleInput[3] = ['B','F','M','D']
# puzzleInput[4] = ['T','J','G','W','V','Q','L']
# puzzleInput[5] = ['W','D','G','P','V','F','Q','M']
# puzzleInput[6] = ['V','Z','Q','G','H','F','S']
# puzzleInput[7] = ['Z','S','N','R','L','T','C','W']
# puzzleInput[8] = ['Z','H','W','D','J','N','R','M']
# puzzleInput[9] = ['M','Q','L','F','D','S']

f = open("D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day5\Day5FullInput.txt")
moveList = f.readlines()
#split box map
boxMap = moveList[0:7]
numberOfStacks = moveList[8]
for line in boxMap:
    i = 0
    while i < len(line):
        puzzleInput[i].append(line(i))
        i+=1

print("break here")
#list.strip()
#list.reverse()

#Move boxes
for instruction in moveList:
    numberOfBoxes,origin,destination = map(int,re.split('move|from|to',instruction.strip())[1:4])
    while (numberOfBoxes > 0):
        puzzleInput[destination].append(puzzleInput[origin].pop())
        numberOfBoxes -=1 

#Print box labeled on top of box stack
i = 0
while i < len(puzzleInput):
    print(puzzleInput[i+1][len(puzzleInput[i+1])-1])
    i += 1
