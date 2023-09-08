l_check = []
def mix(num,list,S,B,i):
    if num == 0 : 
        return "check"
    length = len(list)
    temp = num
    num = bi(num,length-1)
    if int(num[i]) == 1:
        S *=(int(list[i][0]) )
    B +=(int(list[i][1])*int(num[i]))
    if i == length-1 :
        if S!= 1 and B!=0:
            l_check.append(abs(B-S))
        return mix(temp-1,list,1,0,0)
    else:
        return mix(temp,list,S,B,i+1)

def bi(num,e):
    if e==0 or e<0:
        return str(num)
    elif num//(2**e) ==0 or num//(2**e) == 1:
        return str(num//(2**e))+bi(num%(2**e),e-1)

inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    inp[i] = inp[i].split(" ")
mix((2**len(inp))-1,inp,1,0,0)
print(min(l_check))