
map = []
paths = [] # (risk, py, px)
move = [] # (y,x)

def eval_move(y1, x1, y2, x2):
    global xd,yd
    currisk,py,px = list(paths[y1][x1])
    nr,ny,nx = list(paths[y2][x2])
    newrisk = currisk + map[y2][x2]
    if ((nr == 0) or (newrisk < nr)):
        #print(f"Lowering risk at ({x2},{y2}) from {nr} to {newrisk}")
        paths[y2][x2] = ((newrisk,y1,x1))
        move.append((y2,x2))

with open('day15input.txt', 'r') as fp:
    for line in fp:
        row = [int(x) for x in line.strip()]
        #print(row)
        map.append(row)

#print(map)
xd = len(map[0])
yd = len(map)
print(f"dimenstions: {xd},{yd}")
for y in range(yd):
    paths.append([((0,0,0))]*xd)


move.append((0,1)) # move right
paths[0][1] = ((map[0][1],0,0))
move.append((1,0)) # move down
paths[1][0] = ((map[1][0],0,0))

while(len(move)):
    y,x = list(move.pop())
    print(f"({x},{y}) {len(move)}")

    if (x<xd-1): # right
        eval_move(y, x, y, x+1)
    #if (x>0): #left
    #    eval_move(y, x, y, x-1)
    if (y<yd-1): # down
        eval_move(y, x, y+1, x)
    #if (y>0): # up
    #    eval_move(y, x, y-1, x)


print(map)
print(paths)
danger,y,x = paths[yd-1][xd-1]
y = yd-1
x = xd-1
while (x or y):
    print(f"Path: ({x},{y})")
    temp,y,x = paths[y][x]
print(f"danger: {danger}")



