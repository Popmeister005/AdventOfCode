f = open('D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day10\Day10Input.txt')
puzzleInput = f.readlines()

cycle = 0
x = 1
firstTime = False
strengthSum = 0
row = ''
col = []
display = []
currentPixel = 0

for line in puzzleInput:
    
    #find instruction
    split = line.split()
    if 'noop' in split:
        instruction = split[0]
        amount = 0
    else:
        instruction = split[0]
        amount = int(split[1])

    #tick up cycle
    processInstruction = True

    while processInstruction:
        #tick up cycle
        cycle += 1
        #draw pixel
        if len(col) == 40:
            display.append(col)
            col = []
        
        if (x == cycle%40) or (x+1 == cycle%40) or (x+2 == cycle%40):
            col.append('#')
        else:
            col.append(' ')

        #print("start of cycle", cycle, x)

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
                x += amount
            else:
                firstTime = True

        #print("end of cycle", cycle, x)

display.append(col)

print(strengthSum)
for row in display:
    print()
    for col in row:
        print(col,end = '')
