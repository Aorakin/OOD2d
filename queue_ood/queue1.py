class Queue():
    def __init__(self,ls=None):
        if ls == None : self.items =[]
        else:self.items = ls

    def deQueue(self):
        return self.items.pop(0)
    def enQueue(self,inp): self.items.append(inp)
    def front(self): return self.items[0]
    def size(self): return len(self.items)
    def isEmpty(self): 
        if self.items == [] : return True
        else : return False
    def formatPrint(self):
        if self.items == [] :return "Empty"
        else: return ", ".join(self.items)

newqueue = Queue()
tempqueue = Queue()
numIn = input("Enter Input : ").split(",")
result = None
for i in numIn :
    if i[0] == 'E':
        newqueue.enQueue(i[2])
        print(newqueue.formatPrint())
    elif i[0] =='D':
        if newqueue.isEmpty():
            print("Empty")
        else:
            print(newqueue.front(),end = "")
            tempqueue.enQueue(newqueue.deQueue())
            print(f' <- {newqueue.formatPrint()}')
print(f'{tempqueue.formatPrint()} : {newqueue.formatPrint()}')

    