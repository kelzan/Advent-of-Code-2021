digits = [0] * 9

with open('day8input.txt', 'r') as fp:
    for line in fp:
        fields = line.strip().split(" | ")
        output = fields[1].split()
        X = [len(x) for x in output]
        for x in X:
            digits[x] += 1


answer = digits[2] + digits[3] + digits[4] + digits[7]
print(f"answer: {answer}")