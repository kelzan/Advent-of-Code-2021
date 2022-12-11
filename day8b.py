class display:
    def __init__(self, initvals):
        self.decode = {}
        temp = [x for x in initvals if (len(x) == 2)]
        self.decode[temp[0]] = 1
        temp = [x for x in initvals if (len(x) == 3)]
        self.decode[temp[0]] = 7
        temp = [x for x in initvals if (len(x) == 4)]
        self.decode[temp[0]] = 4
        temp = [x for x in initvals if (len(x) == 7)]
        self.decode[temp[0]] = 8

        temp = [x for x in initvals if (len(x) == 6)]
        four = self.get_code(4)
        for x in temp:
            if (self.is_subarray(four,x)):
                self.decode[x] = 9
                temp.remove(x)
                break
        one = self.get_code(1)
        for x in temp:
            if (self.is_subarray(one,x)):
                self.decode[x] = 0
                temp.remove(x)
                break
        self.decode[temp[0]] = 6

        temp = [x for x in initvals if (len(x) == 5)]
        #print(temp)
        for x in temp:
            if (self.is_subarray(one,x)):
                self.decode[x] = 3
                temp.remove(x)
                break
        nine = self.get_code(9)
        for x in temp:
            if (self.is_subarray(x,nine)):
                self.decode[x] = 5
                temp.remove(x)
                break

        self.decode[temp[0]] = 2        
        
        #print(self.decode)

    def is_subarray(self, inner, outer):
        #print(f"inner: {inner}, outer: {outer}")
        for i in inner:
            if i not in outer:
                #print(f"{i} is not in {outer}")
                return False
        return True

    def get_code(self, number):
        for key, value in self.decode.items():
            if number == value:
                return key
        print("key doesn't exist")

    def decode_display(self, display):
        return(self.decode[display])

digits = [0] * 9

answer = 0
with open('day8input.txt', 'r') as fp:
    for line in fp:

        fields = line.strip().split(" | ")

        initdisp = [''.join(sorted(x)) for x in fields[0].split()]
        mydisp = display(initdisp)

        output = [''.join(sorted(x)) for x in fields[1].split()]
        for x in output:
            digitval = mydisp.decode_display(x)
        outval = (mydisp.decode_display(output[0]) * 1000) + (mydisp.decode_display(output[1]) * 100) + (mydisp.decode_display(output[2]) * 10) + mydisp.decode_display(output[3])
        print(f"outval: {outval}")
        answer += outval

print(f"answer: {answer}")