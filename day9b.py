import numpy as np
xdim = 0
ydim = 0

def printmap(pm):
    print()
    for y in range(pm.shape[0]):
        for x in range(pm.shape[1]):
            print(int(pm[y,x]), end="")
        print()

def replace_val(arr, old, new):
    arr = np.where(arr == old, new, arr)
    printmap(arr)

def mark(y, x, b_num):
    #print(f"[{y},{x}]")
    basin[y,x] = b_num
    #printmap(basin)
    if ((x > 0) and (basin[y,x-1] == 0)):
        mark(y,x-1,b_num)
    if ((x < xdim-1) and (basin[y,x+1] == 0)):
        mark(y,x+1,b_num)
    if ((y > 0) and (basin[y-1,x] == 0)):
        mark(y-1,x,b_num)
    if ((y < ydim-1) and (basin[y+1,x] == 0)):
        mark(y+1,x,b_num)

inarray = []

with open('day9input.txt', 'r') as fp:
    for line in fp:
        row = [int(x) for x in list(line.strip())]
        inarray.append(row)
#basin = deepcopy(depth)
depth = np.array(inarray)

xdim = depth.shape[1]
ydim = depth.shape[0]
print(f"dim: ({xdim},{ydim})")

basin = np.where(depth == 9, 1, 0)

# printmap(depth)
# printmap(basin)

answer = 0
basin_num = 2
#print(depth.shape)
#print(basin.shape)
for y in range(ydim):
    for x in range(xdim):
        if (basin[y,x] == 0):
            mark(y,x,basin_num)
            basin_num += 1 



cntvals = []
for x in range(2,basin_num):
    cntvals.append(np.count_nonzero(basin == x))


cntvals.sort(reverse = True)
print(f"{cntvals}")
answer = cntvals[0] * cntvals[1] * cntvals[2]
print(f"answer: {answer}")

