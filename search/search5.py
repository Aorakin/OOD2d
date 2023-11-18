def distance(XY,P2 = [0,0]):
    x,y = XY[0],XY[1]
    x2,y2 = P2[0],P2[1]
    return square_root(0.00001,(x-x2)**2+(y-y2)**2)

def square_root(presition,num):
    left,right = 0,num
    while right - left >=presition:
        mid = (right+left)/2
        if mid*mid > num :
            right = mid
        else :
            left = mid
    return (right+left)/2

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
        
    left,right = ind-1,ind+1
    for i in range(len(point)):
        if left == -1 and right == len(point):
            break
        elif right >=len(point):
            print(f"{point[ind]} -> {point[left]} | The distance is ",end="")
            print("{:.4f}".format(distance(point[ind],point[left])))
            ind = left
            left-=1
        elif left <= -1:
            print(f"{point[ind]} -> {point[right]} | The distance is ",end="")
            print("{:.4f}".format(distance(point[ind],point[right])))
            ind = right
            right+=1
        elif distance(point[ind],point[left]) < distance(point[ind],point[right]):
            print(f"{point[ind]} -> {point[left]} | The distance is ",end="")
            print("{:.4f}".format(distance(point[ind],point[left])))
            ind = left
            left-=1
        elif left > -1 and distance(point[ind],point[left]) >= distance(point[ind],point[right]) :
            print(f"{point[ind]} -> {point[right]} | The distance is ",end="")
            print("{:.4f}".format(distance(point[ind],point[right])))
            ind = right
            right+=1
        

inp = input("Enter a list of points: ").split("/")
allPoint = inp[0].split(",")
for i in range(len(allPoint)):
    allPoint[i] = allPoint[i].split(" ")
    allPoint[i] = list(map(float,allPoint[i]))
inp[1] = list(map(float,inp[1].split(" ")))
travel(inp[1],allPoint)