class Stack :

    def __init__(self,list = None) :
        if list == None : self.item = []
        else : self.item = list
    def isEmpty(self) :
        if self.item ==[]:return True
        else: return False
    def push(self,data) :self.item.append(data)
    def pop(self) :return self.item.pop()
    def size(self) :return len(self.item)
    def peek(self) :return self.item[-1]

def checkOperator(op):
    dic= {"*": 3,"/":3,"(":1 ,"+" :2,"-":2,")":20}
    return dic[op]
def formatItem(item):
    return "".join(item)

def infix2postfix(exp) :
    s = Stack()
    opstack =Stack()
    index = 0
    check = True
    length = len(exp)
    while check:
        if exp[index] not in "+-*/()":
            s.push(exp[index])
        else :
            pri = checkOperator(exp[index])
            if opstack.size()== 0:
                opstack.push(exp[index])
            elif pri <= checkOperator(opstack.peek()) and opstack.size() > 0 and exp[index]!="(":
                while pri <= checkOperator(opstack.peek()):
                    s.push(opstack.pop())
                    if opstack.size() == 0: break
                opstack.push(exp[index])
            elif exp[index] == ")" and opstack.size() !=0:
                while opstack.peek()!="(": 
                    s.push(opstack.pop())
                opstack.pop()
            else: opstack.push(exp[index])
        index+=1
        if index == length :
            if opstack.size() != 0:
                while opstack.size()!=0:
                    s.push(opstack.pop())
            check =False
    
    return  formatItem(s.item)
def infixToPrefix(exp):
    string = ""
    stack =  Stack()
    length = len(exp)
    dic= {"*": 3,"/":3,"(":1 ,"+" :2,"-":2}
    for i in range(length):
        if exp[i] not in "*+-/)(":
            string += exp[i]
        elif exp[i] == ")":
            print(string)
            while not stack.isEmpty() and stack.peek() != "(":
                temp = stack.pop()
                if dic[temp] >dic[stack.peek()] and not stack.isEmpty() and stack.peek() != "(":
                    string = string[:-2]+  temp + string[-2:]
                else:string = temp + string 
            stack.pop()
        else:
            while not stack.isEmpty() and dic[exp[i]] < dic[stack.peek()]:
                # print(string[:-2],stack.peek())
                string = stack.pop() + string
            stack.push(exp[i])
    while not stack.isEmpty():
        temp = stack.pop()
        if not stack.isEmpty() and dic[temp] >dic[stack.peek()]  and stack.peek() != "(":
            string = string[:-2]+  temp + string[-2:]
        else:string = temp + string 
    print(string)
            
print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infixToPrefix(token))
#a/b*(c-d*e/f+(g-h))*i
# ab/cde*f/-gh-+*i*
