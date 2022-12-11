import sys

map = []

unvisited_nodes = []
shortest_path = {}
previous_nodes = {}

myfunc = lambda x: x + 1 if (x<9) else 1

with open('day15input.txt', 'r') as fp:
    for line in fp:
        row = [int(x) for x in line.strip()]
        #print(row)
        fullrow = row
        for i in range(4):
            frow = [myfunc(x) for x in row]
            fullrow = fullrow + frow
            row = frow
        #print(row)
        map.append(fullrow)

orig_y = len(map)
for i in range(4):
    start = len(map) - orig_y
    for j in range(orig_y):
        newrow = [myfunc(x) for x in map[start]]
        map.append(newrow)
        print(f"derived from row {start} is {newrow}")
        start += 1

#print(map)
#sys.exit()
xd = len(map[0])
yd = len(map)
print(f"dimensions: {xd},{yd}")
#sys.exit()
for y in range(yd):
    for x in range(xd):
        unvisited_nodes.append((y,x))
print(unvisited_nodes)

max_value = sys.maxsize
for node in unvisited_nodes:
    shortest_path[node] = max_value

shortest_path[(0,0)] = 0
neighbors = []

while unvisited_nodes:
    if (len(unvisited_nodes))%100 == 0:
        print(len(unvisited_nodes))
    current_min_node = None
    # Find the node with the lowest value and make it the 'current' one
    for node in unvisited_nodes:
        if current_min_node == None:
            current_min_node = node
        elif shortest_path[node] < shortest_path[current_min_node]:
            current_min_node = node
    # Now visit all of the neighbors
    neighbors.clear()
    y,x = list(current_min_node)
    #print(f"current: {current_min_node}")
    if (x<xd-1): # right
        neighbors.append((y, x+1))
    if (x>0): #left
        neighbors.append((y, x-1))
    if (y<yd-1): # down
        neighbors.append((y+1, x))
    if (y>0): # up
        neighbors.append((y-1,x))
    for neighbor in neighbors:
        #print(neighbor,neighbor[1],neighbor[0])
        tentative_value = shortest_path[current_min_node] + map[neighbor[0]][neighbor[1]]
        if tentative_value < shortest_path[neighbor]:
            shortest_path[neighbor] = tentative_value
            previous_nodes[neighbor] = current_min_node
    unvisited_nodes.remove(current_min_node)

print(f"distance: {shortest_path[(yd-1,xd-1)]}")





