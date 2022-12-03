f = open("Day2Input.txt")
input = f.readlines()

paperSize = lambda l,w,h: 2*l*w + 2*w*h + 2*h*l + min(l*w,h*w,l*h)
ribbonLength = lambda l,w,h: min(2*l+2*w, 2*w+2*h, 2*h+2*l) + l*w*h

totalArea = 0
totalRibbon = 0

for line in input:
    l,w,h = map(int, line.split("x"))
    totalArea = totalArea + paperSize(l,w,h)
    totalRibbon = totalRibbon + ribbonLength(l,w,h)

print(totalArea)
print(totalRibbon)
