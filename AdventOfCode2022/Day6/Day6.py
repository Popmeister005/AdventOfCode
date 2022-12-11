f = open('D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day6\Day6.txt')
puzzleInput = f.readline()
i = 0

while i < len(puzzleInput):
    if (puzzleInput[i]!=puzzleInput[i+1] and puzzleInput[i]!=puzzleInput[i+2] and puzzleInput[i]!=puzzleInput[i+3])and (puzzleInput[i+1]!=puzzleInput[i+2] and puzzleInput[i+1]!=puzzleInput[i+3]) and (puzzleInput[i+2]!=puzzleInput[i+3]):
        print(i+3+1)
        break
    i+=1

print(i)