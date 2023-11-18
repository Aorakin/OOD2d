def bubble(list):
    length = len(list)
    for i in range(length-1):
        for j in range(length-1):
            if list[j] < list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

def insertion(list):
    length = len(list)
    for i in range(length-1):
        ele = list[i]
        for j in range(i,-1,-1):
            if ele < list[j-1] and j>0 :
                list[j] = list[j-1]
            else: 
                list[j] = ele
                break

def straight(list):
    length = len(list)
    for i in range(length-1):
        maxi = list[0]
        ind = 0
        for j in range(length-i):
            if maxi < list[j] :
                maxi = list[j]
                ind = j 
        list[j],list[ind] = list[ind],list[j] 

def shell(list,increment):
    length = len(list)
    for i in increment:
        for j in range(i,length):
            ele = list[j]
            for k in range(j,-1,-i):
                if ele < list[k-i] and k >=i:
                    list[k] = list[k-i]
                else:
                    list[k] = ele
                    break


def mergesort(list,left,right):
    mid = (left+right)//2
    if left < right:
        mergesort(list,left,mid)
        mergesort(list,mid+1,right)
        merge(list,left,mid,right)

def merge(list,start,mid,end):
    runleft = start
    runright = mid+1
    result = []
    while runleft <= mid and runright <= end: 
        if list[runleft] < list[runright]:
            result.append(list[runright])
            runright+=1
        else:
            result.append(list[runleft])
            runleft+=1
    while runleft <= mid :
        result.append(list[runleft])
        runleft+=1
    while runright <=end:
        result.append(list[runright])
        runright+=1
    count = start
    for i in result:
        list[count] = i
        count+=1

newlist = [9,4,922,3,46,47,84,"4535",445,7686,3425,7,1,35,7,3,26]
mergesort(newlist,0,len(newlist)-1)
print(newlist)