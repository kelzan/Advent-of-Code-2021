
ones = [0] * 12
zeros = [0] * 12
most = [0] * 12
iter = 0
curnums = []
newnums = []
curnums2 = []

def tally(numarray):
    for i in range(12):
        ones[i] = 0
        zeros[i] = 0
    for num in numarray:    
        for i in range(len(num)):
            if (num[i] == '0'):
                zeros[i] += 1
            elif (num[i] == '1'):
                ones[i] += 1
            else:
                print (f"Problem with line: {num}")

myfile = open('day3input.txt', 'r')
lines = myfile.readlines()
myfile.close()

for line in lines:
    line = line.strip()
    curnums.append(line)

bitpos = 0
curnums2 = curnums.copy()

while (len(curnums) > 1):
    tally(curnums)
    for num in curnums:
        if ((ones[bitpos] >= zeros[bitpos]) and (num[bitpos] == '1')):
            newnums.append(num)
        if ((ones[bitpos] < zeros[bitpos]) and (num[bitpos] == '0')):
            newnums.append(num)
    print(f"{bitpos}: # entries before: {len(curnums)}, now: {len(newnums)}")
    curnums = newnums.copy()
    newnums.clear()
    bitpos += 1

ogr = int(curnums[0],2)
print(f"Oxygen Generator rating: {curnums[0]} ({ogr})")

bitpos = 0
while (len(curnums2) > 1):
    tally(curnums2)
    # if (len(curnums2)<10):
    #     print(curnums2)
    for num in curnums2:
        if ((ones[bitpos] < zeros[bitpos]) and (num[bitpos] == '1')):
            newnums.append(num)
        if ((ones[bitpos] >= zeros[bitpos]) and (num[bitpos] == '0')):
            newnums.append(num)
    print(f"{bitpos}: # entries before: {len(curnums2)}, now: {len(newnums)}")
    curnums2 = newnums.copy()
    newnums.clear()
    bitpos += 1

csr = int(curnums2[0],2)
print(f"CO2 Scrubber rating: {curnums2[0]} ({csr})")

answer = csr * ogr
print(f"answer: {answer}")

