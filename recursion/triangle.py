def tri(num,maxnum):
    if num == 1 and maxnum >= 0:
        return "#"*maxnum
    elif num+(2*maxnum) == -1:
        return "_"*(abs(maxnum)-1) + "#"
    if maxnum < 0:
        print("_"*(num+maxnum)+ "#"*(2*abs(maxnum)-num))
        return tri(num+1,maxnum)
    else:
        print("_"*(num-1) + "#"*(maxnum-num+1) )
        return tri(num-1,maxnum)
inp = input("enter :")

print(tri(abs(int(inp)),int(inp)))