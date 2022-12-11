

binary = ""
version_sum = 0
stack = []

def unpack(startpos):
    global version_sum
    stack_pointer = len(stack)
    curpos = startpos
    #print(f"starting curpos {curpos}")
    version = int(binary[curpos:curpos+3],2)
    curpos += 3
    version_sum += version
    typeid = int(binary[curpos:curpos+3],2)
    curpos += 3
    #print(f"Version: {version}, typeid: {typeid}, curpos: {curpos}")
    if (typeid == 4):
        literal = ""
        while True:
            last = binary[curpos]
            literal += binary[curpos+1:curpos+5]
            #print(f"last: {last}, literal: {literal}")
            curpos += 5
            if last == "0":
                break
        litval = int(literal,2)
        print(f"Version: {version}, typeid: {typeid}, curpos: {curpos}, literal: {litval}")
        stack.append(litval)
    else:
        ltype = binary[curpos]
        curpos += 1
        if (ltype == "1"):
            numsub = int(binary[curpos:curpos+11],2)
            #print(binary[curpos:curpos+11])
            print(f"Version: {version}, typeid: {typeid}, number of subs: {numsub}, curpos: {curpos}")
            curpos += 11
            for sub in range(numsub):
                sublen = unpack(curpos)
                curpos += sublen
        else:
            numsubbits = int(binary[curpos:curpos+15],2)
            #print(binary[curpos:curpos+11])
            print(f"Version: {version}, typeid: {typeid}, number of sub bits: {numsubbits}, curpos: {curpos}")
            curpos += 15
            totalsubbits = 0
            while (totalsubbits < numsubbits):
                sublen = unpack(curpos)
                curpos += sublen
                totalsubbits += sublen
            #print("BLAH!")
        # Now process the stack operation
        if (typeid == 0):
            opval = 0
            while (len(stack) > stack_pointer):
                opval += stack.pop()
        elif (typeid == 1):
            opval = 1
            while (len(stack) > stack_pointer):
                opval *= stack.pop()
        elif (typeid == 2):
            temp = []
            while (len(stack) > stack_pointer):
                temp.append(stack.pop())
            opval = min(temp)
        elif (typeid == 3):
            temp = []
            while (len(stack) > stack_pointer):
                temp.append(stack.pop())
            opval = max(temp)
        elif (typeid == 5): # greater than
            second = stack.pop()
            first = stack.pop()
            if (first > second):
                opval = 1
            else:
                opval = 0
        elif (typeid == 6): # less than
            second = stack.pop()
            first = stack.pop()
            if (first < second):
                opval = 1
            else:
                opval = 0
        elif (typeid == 7): # equal to
            second = stack.pop()
            first = stack.pop()
            if (first == second):
                opval = 1
            else:
                opval = 0
        else:
            print(f"Bad typeid: {typeid}")       
        stack.append(opval)

    packet_length = curpos - startpos
    #print(f"curpos: {curpos}, startpos: {startpos}, packet_length: {packet_length}")
    print(stack)
    return(packet_length)

data = open("day16input.txt").read().strip()

htob = lambda x: bin(int(x,16))[2:].zfill(4)

binary = ''.join([htob(x) for x in data])
#print(binary)

unpack(0)

#print(f"Version sum: {version_sum}")
print(f"Answer: {stack[0]}")