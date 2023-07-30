class Queue():
    def __init__(self,maxval = 1000,ls = None):
        if ls == None : self.items = []
        else : self.items = ls
        self.max_val = maxval
    def enQueue(self,inp): self.items.append(inp)
    def deQueue(self):return self.items.pop(0)
    def size(self):return len(self.items)
    def front(self):return self.items[0]
    def isEmpty(self):
        if self.items == []: return True
        else : return False

step = input("input : ").split(",")
newQueue = Queue()
errD = 0
errI = 0
count = 0
num = ''
for i in step:
    if len(i)>=3:
        for x in i : 
            if x.isdigit():
                num +=x
    elif not i[1].isdigit(): num='0'
    else:num =i[1]
    if i[0] =='E':
        for j in range(int(num)):
            newQueue.enQueue('*'+str(count))
            count+=1
        formatstring = "Enqueue : "
    elif i[0] =='D':
        if  newQueue.isEmpty():errD +=int(num)
        else: 
            if int(num)<=newQueue.size():
                for k in range(int(num)):
                    newQueue.deQueue()
            else: 
                errD+=(int(num)-newQueue.size())
                while not newQueue.isEmpty():
                    newQueue.deQueue()
        formatstring = "Dequeue : "
    else : 
        errI+=1
        formatstring = ""
    print(f"Step : {i}\n{formatstring}{newQueue.items}\nError Dequeue : {errD}\nError input : {errI}")
    print("--------------------")
    num = ''
            