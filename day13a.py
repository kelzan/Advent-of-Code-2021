import numpy as np
from operator import itemgetter
import re

indots = []
folds = []

with open('day13input.txt', 'r') as fp:
    for line in fp:
        pairs = line.strip().split(",")
        if (len(pairs) == 2):
            indots.append((int(pairs[1]),int(pairs[0])))
        else:
            match = re.search(r"^fold along (.)=(.*)", line)
            if match:
                #print(f"found! {match.group(0)} {match.group(1)} {match.group(2)}")
                folds.append((match.group(1),int(match.group(2))))

print (indots)
print (folds)
max_x = max([x[1] for x in indots])
max_y = max([x[0] for x in indots])

arr = np.array(list(range(25))).reshape(5,5)
print(arr)
print(arr[0:2,0:5])
print(arr[2:4,0:5])
print(arr[0:2,0:5]+arr[2:4,0:5])
print(arr[(3,2)])
print(f"dim: {max_y+1},{max_x+1}")
paper = np.zeros((max_y+1,max_x+1))
for dot in indots:
    paper[dot] = 1
print(paper)
foldcnt=1
for fold in folds:
    print(f"Fold #{foldcnt}:")
    foldcnt += 1
    if fold[0] == 'x':
        #print(paper[:,0:fold[1]])
        #print(paper[:,-1:fold[1]:-1])
        paper = paper[:,0:fold[1]] + paper[:,-1:fold[1]:-1]
    if fold[0] == 'y':
        #print(paper[0:fold[1],:])
        #print(paper[-1:fold[1]:-1,:])
        paper = paper[0:fold[1],:] + paper[-1:fold[1]:-1,:]
    print(paper)

for y in range(paper.shape[0]):
    for x in range(paper.shape[1]):
        if paper[y,x] == 0:
            print(".", end="")
        else:
            print("#",end="")
    print()

#answer = np.count_nonzero(paper)
#print(f"answer: {answer}")