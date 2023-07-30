def CountUperLower(mes :str ):
    Upchar = 0
    Lowchar = 0
    listUpchar = []
    listLowchar = []
    for c in mes :
        if c.isupper():
            Upchar +=1
            listUpchar.append(c)
        elif c.islower():
            Lowchar +=1
            listLowchar.append(c)
        else : continue
    return [Upchar,Lowchar,listUpchar,listLowchar]
print(" *** String count ***")
message = input("Enter message : ")
lt = CountUperLower(message)
Uplist = []
Lowlist = []
temp = ''
for i in lt[2]:
    if i not in Uplist:
        Uplist.append(i)
for j in lt[3]:
    if j not in Lowlist:
        Lowlist.append(j)
Uplist.sort()
Lowlist.sort()
print("No. of Upper case characters : "+str(lt[0]))
print("Unique Upper case characters : "+"  ".join(Uplist))
print("No. of Lower case Characters : "+str(lt[1]))
print("Unique Lower case characters : "+"  ".join(Lowlist))
