class Queue():
    def __init__(self,ls = None):
        if ls == None: self.items = []
        else: self.items = ls
    def enqueue(self,*ID):self.items.append(ID)
    def dequeue(self):return self.items.pop(0)
    def isEmpty(self):
        if self.items == []:return True
        else: return False
    def size(self): return len(self.items)
    def front(self) : return self.items[0]

Fpos = None
checkExit = 1
checksize = 1
newinput = input("Enter width, height, and room: ").split(" ")
width,height = int(newinput[0]),int(newinput[1])
checkmap = newinput[2].split(",")
Fypos = 0
oper = [(0,-1),(1,0),(0,1),(-1,0)]
if height == len(checkmap):
    for i in checkmap:
        if len(i)!=width:
            checksize = 0
else : 
    checksize = 0
newmap = []
for i in checkmap:
    temp =[]
    for j in i:
        if j == 'F':
            Fpos=(i.index('F'),Fypos)
        temp.append(j)
    newmap.append(temp)
    Fypos+=1
if Fpos==None : 
    checkstart = 0
else : 
    x,y = Fpos[0],Fpos[1]
    checkstart = 1
    newQueue = Queue([Fpos])
if checksize and checkstart:
    while checkExit:
        if not newQueue.isEmpty():
            print(f"Queue: {newQueue.items}")
            x,y = newQueue.front()[0],newQueue.front()[1]
            newQueue.dequeue()
        elif checkExit!=0 :
            print("Cannot reach the exit portal.")
            break
        for i in oper :
            temp1 = x
            temp2 = y
            temp1+=i[0]
            temp2+=i[1]
            if temp1>width-1 or temp2>height-1 or temp2 <0 or temp1 <0:
                continue
            elif newmap[temp2][temp1] =="_":
                newmap[temp2][temp1] = "."
                newQueue.enqueue(temp1,temp2)
            elif newmap[temp2][temp1] == "O":
                print("Found the exit portal.")
                checkExit = 0
                break
else: print("Invalid map input.")