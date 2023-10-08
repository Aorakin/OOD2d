def swap(list,index,max_ind,stop):
    if stop <= 0:
        return list
    if list[max_ind] <= list[index]  :
        max_ind = index
    if index == stop   :
        if max_ind != stop:
            list[max_ind],list[stop] = list[stop],list[max_ind]
            print(f"swap {list[max_ind]} <-> {list[stop]} : {list}")
        stop-=1
        index = 0
        max_ind = 0
    swap(list,index+1,max_ind,stop)
    return list

inp = input("Enter Input : ").split(" ")
inp = list(map(int,inp))
print(swap(inp,0,0,len(inp)-1))