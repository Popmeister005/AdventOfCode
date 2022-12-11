f = open('D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day6\Day6.txt')
puzzleInput = f.readline()
i = 0

while i < len(puzzleInput):
    currentSet = list(set(puzzleInput[i:i+14]))
    print(currentSet)
    if len(currentSet) ==14:
        print(i+14)
        break

    i+=1

print(i+14)