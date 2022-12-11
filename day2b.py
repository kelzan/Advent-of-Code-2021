myfile = open('day2input.txt', 'r')
lines = myfile.readlines()
myfile.close()
horz = 0
vert = 0
aim = 0
for line in lines:
    x = line.split(" ")
    direction = x[0]
    amount = int(x[1])
    print(f"d: {direction}, a: {amount}, {horz} {vert}")
    if (direction == "forward"):
        horz += amount
        vert += (aim * amount)
    elif (direction == "down"):
        aim += amount
    elif (direction == "up"):
        aim -= amount
    else:
        print (f"Problem with line: {line}")
answer = horz * vert
print(f"horizontal: {horz}, vertical: {vert}, aim: {aim}, product: {answer}")