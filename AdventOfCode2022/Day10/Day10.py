def parseInstruction(line):
    split = line.split()
    if 'noop' in split:
        instruction = split[0]
        value = 0
    else:
        instruction = split[0]
        value = int(split[1])
    return instruction, value

f = open('D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day10\Day10InputTest.txt')
puzzleInput = f.readlines()

cycle = 0
x = 1
firstTime = False
strengthSum = 0

for line in puzzleInput:
    
    #find instruction
    instruction, value = parseInstruction(line)

    processInstruction = True

    while processInstruction:
        #tick up cycle
        cycle += 1

        #check if we are 20,60,100,140...
        if (cycle - 20)%40 == 0:
            print("The current Value of X is: ", x)
            print("Cycle count is: ", cycle)
            strengthSum += (cycle*x)
            print("signal strength is: ", cycle*x)

        #handle instruction
        if instruction == 'noop':
            #do nothing
            processInstruction = False

        if instruction == 'addx':
            if firstTime == True:
                firstTime = False
                processInstruction = False
                x += value
            else:
                firstTime = True

print(strengthSum)
    
