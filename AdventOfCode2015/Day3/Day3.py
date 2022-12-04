f = open("D:\CodeProjects\AdventOfCode\AdventOfCode2015\Day3\Day3Input.txt")
puzzleInput = f.readline()

houseMap = {}
x = 0
y = 0

for direction in puzzleInput:
    if direction == ">":
        x +=1
    elif direction == "<":
        x -= 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1

    location = str(x) + ',' + str(y)

    if location in houseMap:
        houseMap[location] += 1
    else:
        houseMap[location] = 1

print(len(houseMap))
