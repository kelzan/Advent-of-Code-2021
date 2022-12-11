
paths = {}
valid_routes = 0

def navigate(route, road):
    global valid_routes
    location = route + [road]
    #route.append(road)
    if (road == "end"):
        print(f"Route found: {location}")
        valid_routes += 1
        return
   
    small_caves = [location.count(x) for x in location if x.islower()]
    max_visits = max(small_caves)
    if (max_visits < 2):
        choices = [x for x in paths[road] if ((x.isupper() or (route.count(x) < 2)) and (x != "start"))]
    else:
        choices = [x for x in paths[road] if (x.isupper() or (x not in route))]

    #print(f"location: {location} has choices {choices} (max visits: {max_visits})")
    for newroad in choices:
        navigate(location, newroad)

    

with open('day12input.txt', 'r') as fp:
    for line in fp:
        first, second = line.strip().split("-")
        if not first in paths:
            paths[first] = []
        paths[first].append(second)
        if not second in paths:
            paths[second] = []
        paths[second].append(first)

print(paths)

route = ["start"]
#print(route)
#print(route[0])
#choices = route[0]
for road in paths["start"]:
    navigate(route, road)

print(f"Valid routes: {valid_routes}")

