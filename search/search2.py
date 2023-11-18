def firstmin(list1,list2):
    ind = 0
    lenght = len(list1)
    for i in list2: 
        if i >=list1[-1]:
            print("No First Greater Value")
        for j in range(ind,lenght):
            if list1[j] > i:
                print(list1[j])
                ind = j
                break
    
def insertion(list):
    for i in range(len(list)):
        element = list[i]
        for j in range(i,-1,-1):
            if list[j-1] > element and j>0:
                list[j] = list[j-1]
            else: 
                list[j] = element
                break
    return list

            





inp = input("Enter Input : ").split("/")
list1 = insertion(list(map(int,inp[0].split(" "))))
list2 = insertion(list(map(int,inp[1].split(" "))))
firstmin(list1,list2)