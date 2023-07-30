class stack():
    def __init__(self,list = None):
        if list == None: self.item =[]
        else : self.item =list
    def push (self, item): return self.item.append(item)
    def pop (self): return self.item.pop()
    def peek(self): return self.item[-1]
    def size(self) : return len(self.item)
def checkmatch(inp,out):
    if (inp == ")" and out == "(") or (inp == "]" and out == "[")or (inp == "}" and  out == "{"):
        return True
    else : return False
string = input("Enter expresion : ")
newstack = stack()
count = 1
for i in range(len(string)):
    if string[i] in '([{' :
        newstack.push(string[i])
    elif newstack.size() == 0 and string[i] in ")}]":
        print(f"{string} close paren excess")
        count = 0
        break
    elif string[i] in ")}]" and checkmatch(string[i],newstack.peek()):
        newstack.pop()
    elif  string[i] in ")}]" and  not checkmatch(string[i],newstack.peek()) :   
        print(f'{string} Unmatch open-close')
        count= 0
        break
if newstack.size() == 0 and count == 1:print(f'{string} MATCH')
elif newstack.size()!= 0 and count: 
        print(f'{string} open paren excess   {newstack.size()} : {"".join(newstack.item)}')
