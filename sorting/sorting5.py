def list_insertion(ind,templist):
    while ind < len(templist):
        ele = templist[ind]
        for i in range(ind,-1,-1):
            if len(templist[i-1]) > len(ele) and i>0  :
                templist[i] = templist[i-1]
            elif (templist[i-1]) == len(ele) and i>0 and templist[i-1] > ele :
                    templist[i] = templist[i-1]
            elif (templist[i-1]) == len(ele) and i>0 and templist[i-1] <= ele:
                    templist[i] = ele
                    break
            else: 
                templist[i] = ele
                break
        ind+=1

def subset(picked,temp,list,checkresult):
    if len(temp) == 0 :
        return picked
    for i in range(1,len(temp)+1):
        subset(picked+[temp[i-1]],temp[i:],list,checkresult)
        result = sum(picked+[temp[i-1]])
        if  result == checkresult:
            list.append(picked+[temp[i-1]])
    return list
        
inp = input("Enter Input : ").split("/")
newlist = list(map(int,inp[1].split(" ")))
allsubset = subset([],newlist,[],int(inp[0]))
if allsubset == [] :
    print("No Subset")
else :
    list_insertion(0,allsubset)
    for i in allsubset:
        print(i)


