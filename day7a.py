def calc_fuel(array,pos):
    return(sum([abs(x-pos) for x in array]))

X = [int(x) for x in open("day7input.txt").read().strip().split(",")]

print(f"max: {max(X)}")
numpos = max(X)

posarray = list(range(numpos))
distarray = [calc_fuel(X,x) for x in posarray]
#print(distarray)
fuel = min(distarray)
horpos = distarray.index(fuel)
print(f"Minimum fuel {fuel} at position {horpos}")