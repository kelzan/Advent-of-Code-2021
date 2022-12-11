NUMDAYS = 256

fishes = [0] * 10

def agefish():
    fishes[9] = fishes[0] # Newborn fish
    fishes[7] += fishes[0] # Restarted fish
    for f in range(9):
        fishes[f] = fishes[f+1]
    fishes[9] = 0

fp =  open('day6input.txt', 'r')
line = fp.readline()
fp.close()

startfish = line.strip().split(",")
for f in startfish:
    fishes[int(f)] += 1

for day in range(NUMDAYS):
    agefish()
    print(f"Day: {day} - {sum(fishes)}")
    print(fishes)

answer = sum(fishes)
print(f"Total fish after {NUMDAYS} days: {answer}")