class MinStack:

    def __init__(self,ls = None):
        if ls == None :self.item = []
        else : self.item = ls
        self.mini = []
        self.minimum = None
    def push(self, val: int) -> None: 
        self.item.append(val)
        if self.mini and val<self.mini[-1]:
            self.minimum = val
        elif self.minimum ==None:
            self.minimum = val

        if self.mini and self.minimum <= self.mini[-1] :
            self.mini.append(self.minimum)
        elif not self.mini:
            self.mini.append(val)
        else  : 
            self.mini.append(self.mini[-1])
        
        self.item.append(val)    
    def pop(self) -> None:
        if self.item != [] :
            self.mini.pop()
            return self.item.pop()
        else:"cannt pop"
    def top(self) -> int:
        if self.item != [] :return self.item[-1]
        else:"cannt return top"
    def getMin(self) -> int:
        return self.mini[-1]
    
test = MinStack()
test.push(1)
test.push(2)
print(test.getMin())