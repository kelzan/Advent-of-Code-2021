myfile = open('day1input.txt', 'r')
lines = myfile.readlines()
myfile.close()

prev_val = 0
num_increase = 0

#for line in lines:
for i in range(len(lines)-2):
    curnum = int(lines[i].strip()) + int(lines[i+1].strip()) + int(lines[i+2].strip())
#    print(f"curnum: {curnum}, ni: {num_increase}")
    if ((i != 1) and (curnum > prev_val)):
        num_increase += 1
    prev_val = curnum

print (f"num increase: {num_increase}")