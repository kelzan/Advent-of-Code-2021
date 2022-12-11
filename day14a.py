
rules = {}
STEPS = 10

with open('day14input.txt', 'r') as fp:
    template = fp.readline().strip()
    fp.readline()
    for line in fp:
        pairs = line.strip().split(" -> ")
        rules[pairs[0]] = pairs[1]

print(template)
print(rules)
print(f"Template: {template}")

for step in range(STEPS):
    polymer = ""
    for i in range(len(template)-1):
        polymer = polymer + template[i] + rules[template[i]+template[i+1]]
    polymer += template[-1]
    print(f"After step {step+1}: {polymer}")
    #print(f"step {step+1}")
    template = polymer

#print(polymer)
freq = {}

for c in polymer:
    if c not in freq:
        freq[c] = 0
    freq[c] += 1

sorted_freq = sorted(freq.items(), key = lambda x: x[1])
print(sorted_freq)
answer = sorted_freq[-1][1] - sorted_freq[0][1]
print(f"answer: {answer}")