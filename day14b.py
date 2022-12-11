from collections import Counter
rules = {}
STEPS = 4

with open('day14input.txt', 'r') as fp:
    template = fp.readline().strip()
    fp.readline()
    for line in fp:
        pairs = line.strip().split(" -> ")
        rules[pairs[0]] = pairs[1]

print(template)
print(rules)
#template = template[2:4]
print(f"Template: {template}")

C1 = Counter()
for i in range(len(template)-1):
    C1[template[i]+template[i+1]] += 1
print(C1)

for t in range(41):

    if t in [10,40]:
        CF = Counter()
        for k in C1:
            CF[k[0]] += C1[k]
        CF[template[-1]] += 1
        print(max(CF.values()) - min(CF.values()))

    C2 = Counter()
    for k in C1:
        #print(f"k: {k} k[0]: {k[0]}, k[1]: {k[1]}, rules[k]: {rules[k]}, C1[k]: {C1[k]}")
        C2[k[0] + rules[k]] += C1[k]
        C2[rules[k]+k[1]] += C1[k]

    C1 = C2
    #print(C1)

# for step in range(STEPS):
#     polymer = ""
#     for i in range(len(template)-1):
#         polymer = polymer + template[i] + rules[template[i]+template[i+1]]
#     polymer += template[-1]
#     print(f"After step {step+1}: {polymer}")
#     #print(f"step {step+1}")
#     template = polymer

# #print(polymer)
# freq = {}

# for c in polymer:
#     if c not in freq:
#         freq[c] = 0
#     freq[c] += 1

# sorted_freq = sorted(freq.items(), key = lambda x: x[1])
# print(sorted_freq)
# answer = sorted_freq[-1][1] - sorted_freq[0][1]
# print(f"answer: {answer}")