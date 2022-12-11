import numpy as np

ventmap = np.zeros(shape=(1000,1000))

with open('day5input.txt', 'r') as fp:
    for line in fp:
        fields = line.strip().split()
        fromdir = fields[0].split(",")
        todir = fields[2].split(",")
        x1 = int(fromdir[0])
        y1 = int(fromdir[1])
        x2 = int(todir[0])
        y2 = int(todir[1])
        #print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
        if (y1>y2):
            y_start = y2
            y_end = y1
        else:
            y_start = y1
            y_end = y2
        if (x1>x2):
            x_start = x2
            x_end = x1
        else:
            x_start = x1
            x_end = x2

        if (x1 == x2): # Vertical line
            for y in range(y_start, y_end+1):
                ventmap[x1, y] += 1
        elif (y1 == y2): # Horizontal line
            for x in range(x_start, x_end+1):
                ventmap[x, y1] += 1
       
print(ventmap)

dangerous = 0
for x in ventmap:
    for y in x:
        #print(y)
        if (y >= 2):
            dangerous += 1

print(f"Dangerous locations: {dangerous}")
