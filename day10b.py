def is_open(c):
    return((c == '(') or (c == '[') or (c == '{') or (c == '<'))

def is_close(c):
    return((c == ')') or (c == ']') or (c == '}') or (c == '>'))

def is_match(open,close):
    return(((open == '(') and (close == ')')) or ((open == '[') and (close == ']')) or ((open == '{') and (close == '}')) or ((open == '<') and (close == '>')))

def get_match(c):
    retval = 'X'
    #print(f"checking {c}")
    if c == '(':
        retval = ')'
    if c == '[':
        retval = ']'
    if c == '{':
        retval = '}'
    if c == '<':
        retval = '>'
    #print(f"retval: {retval}")
    return (retval)

def get_score(c):
    retval = 0
    #print(f"checking {c}")
    if c == ')':
        retval = 1
    if c == ']':
        retval = 2
    if c == '}':
        retval = 3
    if c == '>':
        retval = 4
    #print(f"retval: {retval}")
    return (retval)

def calc_score(arr):
    score = 0
    for x in arr:
        score = (score*5) + get_score(x)
    return (score)

parseline = []
chunks = []

with open('day10input.txt', 'r') as fp:
    for line in fp:
        row = [x for x in list(line.strip())]
        chunks.append(row)

answer = 0
missing = []
scores = []

for chunk in chunks:
    parseline.clear()
    for c in chunk:
        if (is_open(c)):
            parseline.append(c)
        elif (is_close(c)):
            if (len(parseline) == 0):
                #print(f"corrupt, no match for {c}")
                parseline.clear()
                break
            start_c = parseline.pop()
            if (not is_match(start_c,c)):
                parseline.clear()
                break
    if (len(parseline)):
        missing.clear()
        for c in parseline:
            missing.insert(0,get_match(c))
        print(f"missing: {missing}")
        scores.append(calc_score(missing))

scores.sort()
print(scores)
answer = scores[len(scores)//2]
print(f"answer: {answer}")