def valueoper(operation):
    dic = {"*":4,"/":4,"+":2,"-":2}
    return dic[operation]

def forcalculate(operation,num2,num1):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "/":
        return num1/num2
    elif operation == "*":
        return num1*num2

string = " 3+5 / 2 "
numlist = []
lis = []
stack = []
oper = []
for i in range(len(string)):
    if string[i] != " ":
        lis.append(string[i])
for j in range(len(lis)):
    if lis[j] not in "+-*/":
        stack.append(lis[j])
    else : 
        if oper and valueoper(lis[j]) > valueoper(oper[-1]):
            oper.append(lis[j])
        elif not oper :
            oper.append(lis[j])
        else : 
            stack.append(oper.pop())
            oper.append(lis[j])
while oper != []:
    stack.append(oper.pop())

for k in range(len(stack)):
    if stack[k] not in "*-+/":
        numlist.append(stack[k])
    else: 
        numlist.append(forcalculate(stack[k],int(numlist.pop()),int(numlist.pop())))

print(numlist)
    
    
