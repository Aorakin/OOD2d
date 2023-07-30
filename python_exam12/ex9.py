print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
for i in range(1,num+1):
    for j in range(1,2*num+(2*num-3)+1):
        if j==num+i-1 or j==3*num-i-1 or j==num-i+1 or j == 3*num+i-3 :
            print("*",end='')
        elif (j<num+i-1 and j>num-i+1) or (j>3*num-i-1 and j<3*num+i-3):
            print("+",end='')
        else: print(".",end='')
    print("")
for i in range(num+2,num*3):
    for j in range(1,2*num+(2*num-3)+1):
        if j==i-num or j == 5*num-i-2 :
            print("*",end='')
        elif (j>i-num and j< 5*num-i-2):
            print("+",end='')
        else: print(".",end='')
    print("")

