def bubble(list,count,index):
    if count <= 0:
        return list
    if index+1 < len(list) and list[index] >= list[index+1] :
        list[index],list[index+1] = list[index+1],list[index]
    if index >= len(list):
        count -=1
        index = -1
    bubble(list,count,index+1)
    return list

inp = input("Enter Input : ").split(" ")
inp = list(map(int,inp))
print(bubble(inp,len(inp),0))
