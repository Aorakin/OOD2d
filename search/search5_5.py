def distance(XY,P2 = [0,0]):
    x,y = XY[0],XY[1]
    x2,y2 = P2[0],P2[1]
    return square_root(0.00000001,(x-x2)**2+(y-y2)**2)

def square_root(presition,num):
    left,right = 0,num
    while right - left >=presition:
        mid = (right+left)/2
        if mid*mid > num :
            right = mid
        else :
            left = mid
    result = (right+left)/2
    return "{:.4f}".format(result)

def insertion(list):
    for i in range(len(list)):
        dis_element = distance(list[i])
        element = list[i]
        for j in range(i,-1,-1):
            if distance(list[j-1])> dis_element and j>0:
                list[j] = list[j-1]
            else:
                list[j] = element
                break
    return list

def findindex(list,num):
    i = 0
    while list[i] !=num:
        i+=1
        if i == len(list):
            return None
    return i

def travel(startpoint,point):
    if startpoint not in point:
        print(f"{startpoint} is not in {point}")
        return 
    else:
        insertion(point)
        ind = findindex(point,startpoint)
    lastpoint = startpoint
    point.pop(ind)
    length = len(point)
    for i in range(length):
        mini = [1000000.000,None]
        for j in range(len(point)):
            dis = float(distance(point[j],lastpoint))
            if dis < mini[0]:
                mini = [dis,j]
        print(f"{lastpoint} -> {point[mini[1]]} | The distance is ",end="")
        print("{:.4f}".format(mini[0]))
        lastpoint=point[mini[1]]
        point.pop(mini[1])
    
        
inp = input("Enter a list of points: ").split("/")
allPoint = inp[0].split(",")
for i in range(len(allPoint)):
    allPoint[i] = allPoint[i].split(" ")
    allPoint[i] = list(map(float,allPoint[i]))
inp[1] = list(map(float,inp[1].split(" ")))
travel(inp[1],allPoint)