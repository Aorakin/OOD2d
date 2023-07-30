class Queue():
    def __init__(self,ls = None):
        if ls == None: self.items = []
        else: self.items = ls
    def enqueue(self,ID):self.items.append(ID)
    def dequeue(self):return self.items.pop(0)
    def isEmpty(self):
        if self.items == []:return True
        else: return False
    def size(self): return len(self.items)
    def front(self) : return self.items[0]

newQueue1 = Queue()
newQueue2 = Queue()
check = 0
inpu = input("Enter Input : ")
# if not inpu:
#     exit()
inp = inpu.split("/")
IDinput = inp[0].split(",")
oper = inp[1].split(",")
placed = 0
employees = [employee.split()[1] for employee in IDinput]
for i in oper:
    if i[0] == 'D':
        if newQueue1.isEmpty() :
            print("Empty")
        else :
            print(newQueue1.dequeue())
    elif i[0] =='E':
        while not newQueue1.isEmpty():
            if check and newQueue1.front()[0] != i[2]:
                newQueue2.enqueue(i[2:])
                check = 0
                placed = 1
            elif newQueue1.front()[0] == i[2]:
                check = 1
            newQueue2.enqueue(newQueue1.dequeue())
        if not placed:
            newQueue2.enqueue(i[2:])
        placed = 0
        check = 0
        while not newQueue2.isEmpty():
            newQueue1.enqueue(newQueue2.dequeue())
