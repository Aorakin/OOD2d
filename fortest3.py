def bubble(list):
    length = len(list)
    for i in range(length):
        for j in range(length-1):
            if list[j] >list[j+1]:
                list[j],list[j+1] =list[j+1],list[j]
    return list

def insertion(list):
    for i in range(len(list)):
        ele = list[i]
        for j in range(i,-1,-1):
            print(i,j)
            if  ele <= list[j-1] and j> 0:
                list[j] =list[j-1]
            else:
                list[j] = ele
                break
            
    return list

def sqrt(expec ,num):
    left,right = 0,num
    while right - left > expec:
        mid = (left+right)/2
        if mid*mid > num:
            right = mid
        else:
            left = mid
    return mid
        
    
    
    


newlist = [3,4,7,2,8,1,9]
print(insertion(newlist ))  
print(sqrt(0.0000000001,2))      

