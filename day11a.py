
octomap = []
xd = 0
yd = 0
zapcnt = 0

def printmap(pm):
    xdim = len(pm[0])
    ydim = len(pm)
    print()
    for y in range(ydim):
        for x in range(xdim):
            print(pm[y][x], end="")
        print()

def incmap():
    for y in range(yd):
        for x in range(xd):
            octomap[y][x] += 1

# def locval(loc):
#     return(octomap[loc[1]][loc[0]])

def shine(y,x):
    if (octomap[y][x] > 0):
        octomap[y][x] += 1
    if (octomap[y][x] >= 10):
        zap(y,x)

def zap(y, x):
    global zapcnt
    octomap[y][x] = 0 # ZAP!
    zapcnt += 1
    if (y>0):
        shine(y-1,x)
        if (x>0):
            shine(y-1,x-1)
        if (x<xd-1):
            shine(y-1,x+1)
    if (y<yd-1):
        shine(y+1,x)
        if (x>0):
            shine(y+1,x-1)
        if (x<xd-1):
            shine(y+1,x+1)
    if (x>0):
        shine(y,x-1)
    if (x<xd-1):
        shine(y,x+1)

def scan(y, x):
    if (octomap[y][x]<10):
        return
    else:
        zap(y, x)
    

with open('day11input.txt', 'r') as fp:
    for line in fp:
        #print(line)
        row = [int(x) for x in list(line.strip())]
        octomap.append(row)
xd = len(octomap[0])
yd = len(octomap)

#print(octomap)
printmap(octomap)
for step in range(100):
    incmap()
    #printmap(octomap)
    for y in range(yd):
        for x in range(xd):
            scan(y,x)
    printmap(octomap)

print(f"answer: {zapcnt}")