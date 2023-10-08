def min_to_max(string):
    list = [int(x) for x in string ]
    check = 0
    for i in range(1,len(list)):
        num = list[i]
        for j in range(i,-1,-1):
            if num < list[j-1] and j>0 :
                list[j] = list[j-1]
            else:
                if list[j-1] == num :
                    check = 1
                list[j] = num
                break
    return [list,check]

def max_to_min(string):
    list = [int(x) for x in string ]
    check = 0
    for i in range(1,len(list)):
        temp = list[i]
        for j in range(i,-1,-1):
            if temp > list[j-1] and j > 0:
                list[j] = list[j-1]
            else:
                if list[j-1] == temp:
                    check = 1
                list[j] = temp
                break

    return [list,check]

def isRepdrome(list):
    temp = list[0]
    for i in list:
        if temp != i:
            return False
    return True
inp = input("Enter Input : ")
newlist = [int(x) for x in inp ]
tomax = min_to_max(inp)
tomin = max_to_min(inp)
if isRepdrome(newlist):
    print("Repdrome")
elif tomax[0] == newlist :
    if tomax[1]:
        print("Plaindrome")
    else:
        print("Metadrome")
elif tomin[0] == newlist:
    if tomin[1]:
        print("Nialpdrome")
    else:
        print("Katadrome")
else:
    print("Nondrome")

