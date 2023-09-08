class stack():
    def __init__(self,list = None):
        if list == None:
            self.item = []
        else:
            self.item = list
    
    def push(self,inp):
        self.item.append(inp)
    def pop(self):
        return self.item.pop()
    def isEmpty(self):
        if self.item:
            return False
        return True
    def size(self):
        return len(self.item)
    def peek(self):
        return self.item[-1]

inp =  input("Enter input :")
length = len(inp)
newstack = stack()
dict = {")":"(","}":"{","]":"["}
check = 0
for i in range(length):
    if inp[i] in "{[(":
        newstack.push(inp[i])
    elif inp[i] in "}])" :
        if newstack.isEmpty() or ( newstack and dict[inp[i]] != newstack.peek()):
            print(False)
            check = 1
            break
        elif not newstack.isEmpty() and newstack.peek() == dict[inp[i]] :
            newstack.pop()
if newstack.isEmpty() and not check:
    print("true")
elif not check :
    print("false")