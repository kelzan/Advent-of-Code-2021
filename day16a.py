# c = "A"
# s=4
# print(f"{s:04b}")
# hex_as_int = int(c, 16)
# print(f"{hex_as_int}")
# hex_as_binary = bin(hex_as_int)
# print(f"{hex_as_binary}")
binary = ""
version_sum = 0

def unpack(startpos):
    global version_sum
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
    packet_length = curpos - startpos
    #print(f"curpos: {curpos}, startpos: {startpos}, packet_length: {packet_length}")
    return(packet_length)
    #print(f"converting {binary[0:3]}, version {version}")

data = open("day16input.txt").read().strip()

htob = lambda x: bin(int(x,16))[2:].zfill(4)

binary = ''.join([htob(x) for x in data])
print(binary)

unpack(0)
# numbits = (len(binary))
# curbit = 0
# while (curbit < numbits):
#     packet_bits = unpack(0)

print(f"Version sum: {version_sum}")