class Stack():
    def __init__(self, ls = None):
        if ls == None :self.item = []
        else :self.item = ls

    def push(self,i):self.item.append(i)
    def pop(self):return self.item.pop()
    def isEmpty(self):
        if self.item ==[]:return True
        else: return False
    def size(self):return len(self.item)
    def peek(self):return self.item[-1]

def checkOperator(num1,num2,op):
    if op == "*": return num2*num1
    elif op == "+":return num2+num1
    elif op == "-" :return num2-num1
    elif op == "/" : return num2/num1

def postFixeval(st):
    s = Stack()
    length = len(st)
    for i in range(length):
        if st[i] <='99' and st[i] >='0' or (st[i][0] =="-" and len(st[i])>1):
            s.push(float(st[i]))
        elif st[i] in "+-*/" :
            s.push(checkOperator(s.pop(),s.pop(),st[i]))
    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split(" "))
print("Answer :  {0:.2f}".format(postFixeval(token)))