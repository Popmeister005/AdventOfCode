import re

f = open("D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day4\Day4Input.txt")
puzzleInput = f.readlines()

containedpair = 0
containedpairlist = []

for pair in puzzleInput:
    numbers = re.split('-|,',pair)
    numbers = [eval(i) for i in numbers]
    if numbers[0] >= numbers[2] and numbers[1] <= numbers[3]:
        containedpair+=1
        containedpairlist.append(numbers)
    elif numbers[2] >= numbers[0] and numbers[3] <= numbers[1]:
        containedpair+=1
        containedpairlist.append(numbers)

print(containedpair)
#for pair in containedpairlist:
#    print(pair)