def find_ind_min(table):
    minval = [table[0][0],0,0] #[val,row,col]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] <= minval[0] :
                minval = [table[i][j],i,j]
    return minval[1]

def find_min(list,colum):
    print(list )
    mini = [list[0],0]
    for i in range(len(list)): 
        if list[i] <= mini[0]:
            mini = [list[i],i]
    print(mini)
    return (mini[1]+1)//colum

def max_in_row(table,row):
    maxi = [table[row][0],0]
    for i in range(len(table[row])):
        if maxi[0]<= table[row][i]:
            maxi = [table[row][i],i]
    return maxi[1]

def find_max_in_col(table):
    tempr = find_ind_min(table)
    col = max_in_row(table,tempr)
    row = len(table)
    maxi = [table[0][col],0]
    for i in range(row):
        if maxi[0] <= table[i][col]:
            maxi = [table[i][col],i]
    return maxi[0]

inp = input("input : ").split(",")
data = list(map(int,inp[1].split(" ")))
table = []
row,col = int(inp[0][0]),int(inp[0][2])
for i in range(row):
    line = []
    for j in range(col):
        if data == [] :
            break
        line.append(data.pop(0))
    table.append(line)
print(find_max_in_col(table))


