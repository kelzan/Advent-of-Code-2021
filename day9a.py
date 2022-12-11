depth = []

with open('day9input.txt', 'r') as fp:
    for line in fp:
        row = [int(x) for x in list(line.strip())]
        depth.append(row)
print(depth)

xdim = len(depth[0])
ydim = len(depth)
print(f"dim: ({xdim},{ydim})")

lows = []
answer = 0

for y in range(ydim):
    for x in range(xdim):
        low = True
        if ((x != 0) and (depth[y][x-1] <= depth[y][x])):
            low = False
            #print(f"check1 {depth[y][x-1]} {depth[y][x]}")
        if ((x != xdim-1) and (depth[y][x+1] <= depth[y][x])):
            low = False
        if ((y != 0) and (depth[y-1][x] <= depth[y][x])):
            low = False
        if ((y != ydim-1) and (depth[y+1][x] <= depth[y][x])):
            low = False
        if (low == True):
            print(f"low found at [{x},{y}] ({depth[y][x]})")
            risk = 1 + depth[y][x]
            answer += risk

print(f"answer: {answer}")
            

