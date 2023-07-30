newlist = [int(x) for x in input("Enter Your List : ").split(" ")]
newlist.sort()
result = []
if len(newlist) <3:
    print("Array Input Length Must More Than 2")
else:
    for i in range (len(newlist) -2):
        for j in range (len(newlist)-1):
            if j == i:
                break
            for k in range(len(newlist))  : 
                if newlist[i]+newlist[j]+newlist[k]==5 and k!=j and k!=i:
                    lt = [newlist[i],newlist[j],newlist[k]]
                    lt.sort()
                    if(lt not in result):
                        result.append(lt)
    print(result)




        
