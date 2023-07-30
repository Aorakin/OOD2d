num = int(input())
for i in range(1,(2+num)+1):
    for j in range (1,4+2*num+1):
        if j<=((4+2*num)/2)-i:
            print("." ,end="")
        elif (j<=((4+2*num)) and j>((4+2*num)/2)) and  (((i==1 or i==2+num) and j>(4+2*num)/2) or (j<3*num or j>=4*num ) ) and i <=((4+2*num)/2):
            print("+" ,end="")
        else:
            print("#" ,end="")
    print("")
for i in range (2+num+1,4+2*num+1):
    for j in range(1,4+2*num+1):
        if j>=(6*2+num)-i:
            print("." ,end="")
        elif ((i==2+num+1 or i==4+2*num) and j<= ((4+2*num)/2)) or  (j==1 or j==2+num)    :
            print("#" ,end="")
        else:
            print("+" ,end="")
    print("")


