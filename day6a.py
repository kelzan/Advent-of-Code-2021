NUMDAYS = 80

class fish:
    def __init__(self, timer=8):
        self.timer = timer

    def age(self):
        offspring = False
        if (self.timer == 0):
            offspring = True
            self.timer = 6
        else:
            self.timer -= 1
        return offspring

fishes = []

def showfish():
    for f in fishes:
        print(f"{f.timer},",end='')
    print()

fp =  open('day6input.txt', 'r')
line = fp.readline()
fp.close()

startfish = line.strip().split(",")
for f in startfish:
    fishes.append(fish(int(f)))

#print("initial: ", end='')
#showfish()

for day in range(NUMDAYS):
    startnum = len(fishes)
    for i in range(startnum):
        baby = fishes[i].age()
        if baby:
            fishes.append(fish())
    #print(f"after {day+1} days: ",end='')
    #showfish()

answer = len(fishes)
print(f"Total fish after {NUMDAYS} days: {answer}")