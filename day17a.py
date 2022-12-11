import re
x1, x2, y1, y2 = [0,0,0,0]
max_y = 0

def in_target(x,y):
    global x1, x2, y1, y2
    #print((x >= x1), (x <= x2), (y >= y1), (y <= y2))
    return ((x >= x1) and (x <= x2) and (y >= y1) and (y <= y2))

def take_shot(xvel, yvel):
    #print("take_shot")
    global max_y
    hit = False
    x,y = [0,0]
    max_y = 0

    while (y >= y1):
        if (y > max_y):
            max_y = y
        if (in_target(x,y)):
            hit = True
        #print(f"current: ({x},{y}), velocity: ({xvel},{yvel}), hit: {hit}, max_y: {max_y}")
        x += xvel
        y += yvel
        if (xvel>0):
            xvel = xvel-1
        yvel = yvel-1
    return (hit)
        


with open('day17input.txt', 'r') as fp:
    for line in fp:
        match = re.search(r"^target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", line.strip())
        if match:
            #print(f"found! {match.group(0)} {match.group(1)} {match.group(2)}")
            print (line.strip())
            print(match.group(0))
            x1 = int(match.group(1))
            x2 = int(match.group(2))
            y1 = int(match.group(3))
            y2 = int(match.group(4))
            print(x1,x2,y1,y2)
            #folds.append((match.group(1),int(match.group(2))))
            break
        else:
            print(f"Bad input: {line}")

# init_x = 6
# init_y = 9

# hit = take_shot(init_x, init_y)
# print(f"hit: {hit}")

global_max = 0
num_hits = 0

for x in range(x2+1):
    for y in range(-300,300):
        if (take_shot(x,y)):
            print(f"hit! ({x},{y}) - max y: {max_y}")
            num_hits += 1
            if (max_y > global_max):
                global_max = max_y

print(f"Num hits: {num_hits}, Max Y: {global_max}")