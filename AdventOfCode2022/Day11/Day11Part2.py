import re

def calculateDenominator(monkeyArray):
    denominator = 1
    for monkey in monkeyArray:
        denominator*=monkey.test
    
    return denominator

class Monkey:
    def __init__(self,item,operation,operationAmount,test,trueMonkey,falseMonkey):
        self.item = item
        self.operation = operation
        self.operationAmount = operationAmount
        self.test = test
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspect = 0
    
    def __str__(self):
        return f"{self.item}, {self.operation}, {self.operationAmount}, {self.test}, {self.trueMonkey}, {self.flaseMonkey}"

f = open('D:\CodeProjects\AdventOfCode\AdventOfCode2022\Day11\Day11Input.txt')
puzzleInput = f.readlines()

monkeyArray = []
numberOfRounds = 10001

for line in puzzleInput:
    #if 'Monkey' in line:
    #    print()
    if 'Starting' in line:
        item = re.split('Starting items: |,',line.strip())[1:]
    elif 'Operation' in line:
        operation,operationAmount = line.strip().split('Operation: new = old')[1].split()
    elif 'Test' in line:
        test = line.strip().split('Test: divisible by ')[1]
    elif 'If true' in line:
        trueMonkey = line.strip().split('If true: throw to monkey')[1]
    elif 'If false' in line:
        falseMonkey = line.strip().split('If false: throw to monkey')[1]
    elif line == '\n':
        monkey = Monkey(list(map(int,item)),operation.strip(),operationAmount.strip(),int(test.strip()),int(trueMonkey.strip()),int(falseMonkey.strip()))
        monkeyArray.append(monkey)

denominator = calculateDenominator(monkeyArray)

for round in range(1,numberOfRounds):
    for monkey in monkeyArray:
        #for item in monkey.item:
        while len(monkey.item):
            #inspect and operate item
            monkey.inspect += 1
            if monkey.operation == '+':
                if monkey.operationAmount == 'old':
                    newItem = int((monkey.item)[0]) + int((monkey.item)[0])
                else:
                    newItem = int((monkey.item)[0]) + int(monkey.operationAmount)
            else:
                if monkey.operationAmount == 'old':
                    newItem = int((monkey.item)[0]) * int((monkey.item)[0])
                else:
                    newItem = int((monkey.item)[0]) * int(monkey.operationAmount)
            
            #get bored and then throw item
            newItem = newItem%denominator #9699690
            monkey.item.pop(0)
            if newItem%monkey.test == 0:
                monkeyArray[monkey.trueMonkey].item.append(int(newItem))
            else:
                monkeyArray[monkey.falseMonkey].item.append(int(newItem))
    
    monkeyNumber = 0
    # print('after round', round)
    # for monkey in monkeyArray:
    #     print('Monkey ',monkeyNumber,': ',monkey.item)
    #     monkeyNumber +=1
    # print()

        #print(monkey)

inspectionCountArray = []
for monkey in monkeyArray:
    inspectionCountArray.append(monkey.inspect)
sortedInspectionArray = sorted(inspectionCountArray)
mostInspections = sortedInspectionArray[-1]
secondMostInpsections = sortedInspectionArray[-2]

print(mostInspections*secondMostInpsections)