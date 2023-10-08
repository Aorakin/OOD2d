def move(n,A,B,C,maxn):
    print(maxn)
    if n == 0 :
        print("from ",A," to",B)
        Blist.append(Alist.pop())
        Alist.append("|")
        return printformat(maxn)
    if Alist[n] == "|" and Alist[0] == "|" and Blist[0] == "|" and Blist[n] == "|":
        return printformat(maxn)
    if Clist[0] == "|":
        print("from ",A," to",C)
        Clist.insert(0,Alist.pop(n-1))
        Alist.append("|")
    # elif Alist[0] == "|":
    #     print("from ",B," to",A)
    #     Alist.insert(0,Blist.pop(n-1))
    #     Blist.append("|")
    else:
        print("from ",A," to",C)
        Blist.insert(0,Alist.pop(n-1))
        Alist.append("|")
    printformat(maxn)
    move(n-1,A,C,B,maxn)
    move(maxn,C,A,B,maxn)

def printformat(index):
    if index == 0:
        print(Alist[index]+"  "+Blist[index]+"  "+Clist[index])
        return 
    print(Alist[index]+"  "+Blist[index]+"  "+Clist[index])
    return printformat(index-1)
inp = int(input("Enter input"))
Alist  = []
Blist = []
Clist = []
for i in range(inp):
    if i == 0:
        Alist.insert(0,"|")
    else :Alist.insert(0,str(i))
    Blist.append("|")
    Clist.append("|")
# print(Alist)
printformat(inp-1)
# move(inp-1,"A","B","C",inp-1)
