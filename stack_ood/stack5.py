class Stack:
    def __init__(self,ls = None,max = 10):
        if ls == None : self.item =[]
        else:self.item =ls
        self.max = max
    def IsEmpty(self):
        if self.item == [] :return True
        else : return False
    def push(self,para):self.item.append(para)
    def pop(self): return self.item.pop()
    def size(self):return len(self.item)
    def peek(self):return self.item[-1]

def parking(max,carIn,act,carAct):
    newstack = Stack()
    newstack.max = max
    tempstack = Stack()
    check = True
    count = 0
    for i in carIn :
        if act == "arrive" and str(carAct)==i:
            print(f"car {carAct} already in soi")
            newstack.push(int(i))
            check = False
        elif carIn == "0" and act == "depart": 
            print(f"car {carAct} cannot depart : Soi Empty")
            check = False 
        elif i!="," and i!="0":newstack.push(int(i))
    length = newstack.size()
    if act == "arrive" and check ==True:
        if newstack.size()+1 > newstack.max:
            print(f"car {carAct} cannot arrive : Soi Full")
            check = False
        else : 
            newstack.push(carAct)
            print(f"car {carAct} arrive! : Add Car {carAct}")
            check = False
    elif act == "depart" and check == True:
        while not newstack.IsEmpty():
            if newstack.peek() == carAct:newstack.pop()
            else :
                tempstack.push(newstack.pop())
                count +=1      
        if count == length :print(f"car {carAct} cannot depart : Dont Have Car {carAct}")
        else : print(f"car {carAct} depart ! : Car {carAct} was remove")
    
    if not tempstack.IsEmpty():
        while not tempstack.IsEmpty():
            newstack.push(tempstack.pop())
    return newstack.item

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
print(parking(m,s,o,n))
### Enter Your Code Here ###