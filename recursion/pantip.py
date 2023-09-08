def WeGoPantip(opj,goal,result):
    if result == goal :
        return 1
    elif (opj == [] and result != goal) or result > goal  :
        return 0
    plus = int(opj[0])
    return WeGoPantip(opj[1:],goal,result+plus) + WeGoPantip(opj[1:],goal,result)

inp = input("Enter Input : ").split("/")
opj = inp[1].split(" ")
print(WeGoPantip(opj,int(inp[0]),0))


