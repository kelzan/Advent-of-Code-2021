class snum:
    def __init__(self, parent = None):
        self.left_is_lit = False
        self.right_is_lit = False
        self.left_litval = 0
        self.right_litval = 0
        self.left_snum = None
        self.right_snum = None
        self.parent = parent

    def set_lit_left(self,litval):
        self.left_is_lit = True
        self.left_litval = litval

    def set_snum_left(self,snumval):
        self.left_is_lit = False
        self.left_snum = snumval

    def set_lit_right(self,litval):
        self.right_is_lit = True
        self.right_litval = litval

    def set_snum_right(self,snumval):
        self.right_is_lit = False
        self.right_snum = snumval

    def init(self,s):
        left = True
        skip = 0
        #print(f"init: {s}")
        for i in range(len(s)):
            #print(f"s[{i}] = {s[i]}")
            if (skip):
                skip -= 1
                continue
            if (i==0):
                if (s[i] != '['):
                    print(f"Parse error, no leading [: {s}")
            elif (s[i] == ','):
                left = False
            elif (s[i] == ']'):
                return(i)
            elif (s[i] == '['):
                if (left):
                    self.left_is_lit = False
                    self.left_snum = snum(self)
                    skip = self.left_snum.init(s[i:])
                    #print(f"i: {i}, skip: {skip}")
                else:
                    self.right_is_lit = False
                    self.right_snum = snum(self)
                    skip = self.right_snum.init(s[i:])
                    #print(f"i: {i}, skip: {skip}")
            else:
                if (left):
                    self.left_is_lit = True
                    self.left_litval = int(s[i])
                else:
                    self.right_is_lit = True
                    self.right_litval = int(s[i])
        return (i)
        #print(f"left: {self.left_is_lit}, {self.left_litval}, {self.left_snum} - right: {self.right_is_lit}, {self.right_litval}, {self.right_snum}")

    def is_lit(self):
        return (self.left_is_lit and self.right_is_lit)

    def do_explode(self):
        sptr = self.parent
        prev = self
        #print("do_explode")
        while (sptr != None):
            #sptr.printme()
            if (sptr.left_is_lit):
                sptr.left_litval += self.left_litval
                break
 #           if ((sptr.parent == None) and (sptr.right_snum == prev)):
            if (sptr.right_snum == prev):
                sptr = sptr.left_snum
                while (not sptr.right_is_lit):
                    sptr = sptr.right_snum
                sptr.right_litval += self.left_litval
                break
            prev = sptr
            sptr = sptr.parent
        sptr = self.parent
        prev = self
        while (sptr != None):
            if (sptr.right_is_lit):
                sptr.right_litval += self.right_litval
                break
#            if ((sptr.parent == None) and (sptr.left_snum == prev)):
            if (sptr.left_snum == prev):
                sptr = sptr.right_snum
                while (not sptr.left_is_lit):
                    sptr = sptr.left_snum
                sptr.left_litval += self.right_litval
                break
            prev = sptr
            sptr = sptr.parent


    def check_explode(self, level=0):
        exploded = False
        if (self.left_is_lit == False):
            if ((level>=3) and self.left_snum.is_lit()):
                #print(f"BOOM! [{self.left_snum.left_litval},{self.left_snum.right_litval}]")
                self.left_snum.do_explode()
                self.left_is_lit = True
                self.left_snum = None
                self.left_litval = 0
                exploded = True
            else:
                exploded = self.left_snum.check_explode(level+1)        
        if ((self.right_is_lit == False) and not exploded):
            if ((level>=3) and self.right_snum.is_lit()):
                #print(f"BOOM! [{self.right_snum.left_litval},{self.right_snum.right_litval}]")
                self.right_snum.do_explode()
                self.right_is_lit = True
                self.right_snum = None
                self.right_litval = 0
                exploded = True
            else:
                exploded = self.right_snum.check_explode(level+1)
        return (exploded)

    def get_snum_from_split(self,val):
        sn = snum(self)
        sn.left_is_lit = True
        sn.left_litval = val//2
        sn.right_is_lit = True
        sn.right_litval = val//2 + val%2
        return(sn)

    def check_split(self):
        split = False
        #print(f"Check_split {self.left_litval},{self.right_litval}")
        if (self.left_is_lit):
            if (self.left_litval > 9):
                #print(f"SPLIT! {self.left_litval}")
                self.left_is_lit = False
                self.left_snum = self.get_snum_from_split(self.left_litval)
                split = True
        else:
            split = self.left_snum.check_split()
        if (not split):
            if (self.right_is_lit):
                if (self.right_litval > 9):
                    #print(f"SPLIT! {self.right_litval}")
                    self.right_is_lit = False
                    self.right_snum = self.get_snum_from_split(self.right_litval)
                    split = True
            else:
                split = self.right_snum.check_split()
        #print(f"split returning: {split}")
        return (split)

    def get_magnitude(self):
        if (self.left_is_lit):
            left = self.left_litval
        else:
            left = self.left_snum.get_magnitude()
        if (self.right_is_lit):
            right = self.right_litval
        else:
            right = self.right_snum.get_magnitude()
        return((3*left) + (2*right))



    def printit(self):
        print("[",end="")
        if (self.left_is_lit):
            print(self.left_litval,end="")
        else:
            self.left_snum.printit()
        print(",",end="")
        if (self.right_is_lit):
            print(self.right_litval,end="")
        else:
            self.right_snum.printit()
        print("]",end="")
        if (self.parent==None):
            print("")

    def printme(self):
        print("[",end="")
        if (self.left_is_lit):
            print(self.left_litval,end="")
        else:
            print("X")
        print(",",end="")
        if (self.right_is_lit):
            print(self.right_litval,end="")
        else:
            print("X")
        print("]",end="")
        print()
    
def add_sn(op1, op2):
    sn = snum()
    sn.left_is_lit = False
    sn.left_snum = op1
    op1.parent = sn
    sn.right_is_lit = False
    sn.right_snum = op2
    op2.parent = sn
    return(sn)

sum = None
with open('day18input.txt', 'r') as fp:
    for line in fp:
        sfn = snum()
        print("Operand: ",end="")
        sfn.init(line.strip())
        sfn.printit()
        #sum = sfn
        if (sum != None):
            sum = add_sn(sum, sfn)
            print("Sum:",end="")
            sum.printit()
        else:
            sum = sfn
        dirty = True
        while (dirty):
            exploded = sum.check_explode()
            if (exploded):
                print("Explode:",end="")
                sum.printit()
                continue
            #break #temp
            split = sum.check_split()
            if (split):
                print("Split: ",end="")
                sum.printit()
            dirty = exploded or split

        print("Resolve: ",end="")
        sum.printit()

sum.printit()
mag = sum.get_magnitude()
print(f"Magnitude: {mag}")
        #sfn.check_explode()
        #sfn.printit()
