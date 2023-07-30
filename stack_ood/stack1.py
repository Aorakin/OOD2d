class stack():
    def __init__(self,list =None):
        if list == None :
            self.item =  []
        else : self.item = list
    def push (self,inp):
        return self.item.append(inp)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def peek(self):
        return self.item[-1]
newlist = input("Enter Input : ")
newstack = stack()
for i in newlist :
    newstack.push(i)
if (newstack.item.count("(") == newstack.item.count(")")) and (newstack.item.count("[")==newstack.item.count("]")):
    print("Parentheses : Matched ! ! !")
else : 
    print("Parentheses : Unmatched  ! !")
        


    