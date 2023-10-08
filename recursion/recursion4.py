def checkperket(mintemp,list,num):
    if num == 0:
        return mintemp
    else:
        temp = mix(num,list)
        if temp == None or temp ==-1 :
            temp = mintemp
        if mintemp<=temp:
            return checkperket(mintemp,list,num-1)
        elif mintemp>temp:
            return checkperket(temp,list,num-1)


def mix(num,list):
    length = len(list)
    if num == length and length != 1 :
        return -1
    else:
        num = bi(num,length-1)
        S = 1
        B = 0
        count = 0
        for i in range(length):
            count += (int(num[i]))
            if int(num[i]) == 1:
                S *=(int(list[i][0]) )
            B +=(int(list[i][1])*int(num[i]))
        if count ==0:
            pass
        else:
            return abs(B-S)
        
def bi(num,e):
    if e==0 or e<0:
        return str(num)
    elif num//(2**e) ==0 or num//(2**e) == 1:
        return str(num//(2**e))+bi(num%(2**e),e-1)




inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    inp[i] = inp[i].split(" ")
print(checkperket(1000,inp,(2**len(inp))-1))
