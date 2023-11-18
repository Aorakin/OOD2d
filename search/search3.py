class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,Maxcollision):
        self.size = size
        self.hashtable = [None for i in range(int(self.size))]
        self.Maxcol = Maxcollision

    def __str__(self):
        for i in range(self.size):
                print("#{0}	{1}".format(i+1,self.hashtable[i]))
        return("---------------------------")

    def isMax(self):
        cur = 0
        while self.hashtable[cur] !=None:
            cur +=1
            if cur == self.size:
                return True
        return False
    
    def sumASCII(self,string):
        result = 0
        for i in string:
            result += ord(i)
        return result 
    
    
    def findindex(self,Key_Val):
        key = Key_Val.key
        ind = self.sumASCII(key)%self.size
        if not self.isMax() and self.hashtable[ind] == None:
            self.hashtable[ind] = Key_Val
        elif not self.isMax() and self.hashtable[ind] != None:
            print(f"collision number 1 at {ind}")
            for i in range(1,self.Maxcol):
                temp = (ind+(i**2))%self.size
                if self.hashtable[temp] == None:
                    self.hashtable[temp] = Key_Val
                    break
                else:
                    print(f"collision number {1+i} at {temp}")
                    if i == self.Maxcol-1:
                        print("Max of collisionChain")
        else:
            pass
print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split("/")
size_maxcol = inp[0].split(" ")
dataInp = inp[1].split(",")
for i in range(len(dataInp)):
    temp = dataInp[i].split(" ")
    dataInp[i] = Data(temp[0],temp[1])
newhash = hash(int(size_maxcol[0]),int(size_maxcol[1]))
for i in range(len(dataInp)):
    if newhash.isMax():
        print("This table is full !!!!!!")
        break
    newhash.findindex(dataInp[i])
    print(newhash)
