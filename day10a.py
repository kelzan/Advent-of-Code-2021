def is_open(c):
    return((c == '(') or (c == '[') or (c == '{') or (c == '<'))

def is_close(c):
    return((c == ')') or (c == ']') or (c == '}') or (c == '>'))

def is_match(open,close):
    return(((open == '(') and (close == ')')) or ((open == '[') and (close == ']')) or ((open == '{') and (close == '}')) or ((open == '<') and (close == '>')))

def get_score(c):
    retval = 0
    #print(f"checking {c}")
    if c == ')':
        retval = 3
    if c == ']':
        retval = 57
    if c == '}':
        retval = 1197
    if c == '>':
        retval = 25137
    #print(f"retval: {retval}")
    return (retval)

parseline = []
chunks = []

with open('day10input.txt', 'r') as fp:
    for line in fp:
        row = [x for x in list(line.strip())]
        chunks.append(row)

answer = 0
for chunk in chunks:
    #print(f"Parsing: {chunk}")
    parseline.clear()
    for c in chunk:
        if (is_open(c)):
            parseline.append(c)
        elif (is_close(c)):
            if (len(parseline) == 0):
                print(f"corrupt, no match for {c}")
                break
            start_c = parseline.pop()
            if (not is_match(start_c,c)):
                print(f"corrupt - wrong character start '{start_c}' for '{c}'")
                score = get_score(c)
                #print(f"score: {score}")
                answer += score
                break
    if (len(parseline)):
        print(f"incomplete: {parseline}")
    #else:
        #print("ok")

print(f"answer: {answer}")