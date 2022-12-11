myfile = open('day3input.txt', 'r')
lines = myfile.readlines()
myfile.close()

ones = [0] * 12
zeros = [0] * 12
iter = 0

for line in lines:
    line = line.strip()
    for i in range(len(line)):
        if (line[i] == '0'):
            zeros[i] += 1
        elif (line[i] == '1'):
            ones[i] += 1
        else:
            print (f"Problem with line: {line}")
#        print(f"  {line[i]} 0:{zeros[i]} 1:{ones[i]}")
#    iter += 1
#    if (iter > 3):
#        break

s_gamma = ""
s_epsilon = ""

for i in range(len(ones)):
    if (ones[i] > zeros[i]):
        s_gamma = s_gamma + "1"
        s_epsilon = s_epsilon + "0"
    elif (ones[i] < zeros[i]):
        s_gamma = s_gamma + "0"
        s_epsilon = s_epsilon + "1"
    else:
        print(f"problem")
    print(f"ones[{i}] = {ones[i]}, zeros[{i}] = {zeros[i]}")

gamma = int(s_gamma,2)
epsilon = int(s_epsilon,2)
print(f"gamma: {s_gamma} ({gamma}), epsilon: {s_epsilon} ({epsilon})")
answer = gamma * epsilon
print(f"answer: {answer}")
