def getDeliveryLocation(direction, x, y):
    """ Update delivery location
        parameters:
            direction - input either >,<,^,V to and update x,y coordinate
            x - x coordinate of location on map
            y - y coordinate of location on map
        return:
            string - map coordinates in string format of 'x,y'
            x - updated x coordinate
            y - update y coordinate
    """ 
    if direction == ">":
        x +=1
    elif direction == "<":
        x -= 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1

    return str(x) + ',' + str(y),x,y

def updateHouseMap(houseMap, location):
    """Update house map with presents at current coordinate
    parameters:
        houseMap - existing Map intended to be a dictionary containing
                    all map coordinates with an existing present
        location - x,y coordinate string in format 'x,y'
    return:
        houseMap - updated Map
    """
    if location in houseMap:
        houseMap[location] += 1
    else:
        houseMap[location] = 1
    return houseMap

"""Main starts here, calculate where santa has visited based on an input"""
f = open("D:\CodeProjects\AdventOfCode\AdventOfCode2015\Day3\Day3Input.txt")
puzzleInput = f.readline()

houseMap = {}
realX = 0
realY = 0
roboX = 0
roboY = 0
i = 0

while i < len(puzzleInput):

    location, realX, realY = getDeliveryLocation(puzzleInput[i], realX, realY)
    houseMap = updateHouseMap(houseMap, location)

    location, roboX, roboY = getDeliveryLocation(puzzleInput[i+1], roboX, roboY)
    houseMap = updateHouseMap(houseMap, location)

    i+=2

print(len(houseMap))
