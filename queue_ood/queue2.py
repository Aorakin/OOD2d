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
qmain = Queue()
cashier1 = Queue(5)
cashier2 = Queue(5)
newinput = input("Enter people and time : ").split(" ")
count1 = 0
count2 = 0
for i in newinput[0] :
    qmain.enQueue(i)
for i in range(int(newinput[1])):
    if count1 == 3 and not cashier1.isEmpty(): 
        cashier1.deQueue()
        if not qmain.isEmpty():
            cashier1.enQueue(qmain.deQueue())
        count1 = 0
    elif cashier1.size() == cashier1.max_val and not qmain.isEmpty():
        cashier2.enQueue(qmain.deQueue())
    elif not qmain.isEmpty():
        cashier1.enQueue(qmain.deQueue())
    if count2 == 2 and not cashier2.isEmpty(): 
        cashier2.deQueue()
        count2 = 0
    if not cashier2.isEmpty() : count2 +=1
    if not cashier1.isEmpty() : count1 +=1
    print(f'{i+1} {qmain.items} {cashier1.items} {cashier2.items}')
    
