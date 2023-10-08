def mergesort(list,left,right):
    med = (left+right)//2
    if left < right :
        mergesort (list,left,med)
        mergesort(list,med+1 , right)
        merge(list,left,med+1,right)

def merge(list,left,med,right):
    result = []
    templeft = left
    endleft = med-1
    while left <= endleft or med <= right:
        if   left <= endleft and med <= right :
            if list[left] <= list[med]:
                result+=[list[left]]
                left +=1
            else:
                result +=[list[med]]
                med +=1
        elif left <= endleft :
            result+= [list[left]]
            left +=1
        elif med <= right :
            result += [list[med]]
            med+=1
    for i in range(len(result)):
        list[templeft] = result[i]
        templeft +=1
        if templeft > right:
            break 
        

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    newlist = []
    for i in range(len(l)):
        newlist.append(l[i])
        mergesort(newlist,0,len(newlist)-1)
        length =len(newlist)
        if  length%2 == 0:
            result = (newlist[length//2]+newlist[length//2-1])/2
        else :
            result = newlist[length//2]
        print(f"list = {l[:i+1]} : median = {float(result)}")
        