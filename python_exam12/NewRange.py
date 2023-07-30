def range(*lt):
    if len(lt) == 3 :
        start = lt[0]
        end = lt[1]
        step = lt[2]
    elif len(lt) ==2:
        start = lt[0]
        end = lt[1]
        step = 1
    elif len(lt) ==1:
        start = 0
        end = lt[0]
        step = 1
    checkstart = str(start)[::-1].find('.')
    checkstep = str(step)[::-1].find('.')
    checkall = max(checkstart, checkstep)
    if  checkall<=0:
        checkall =1 
    list = []
    while start < end:
        list.append(start)
        start+=step
    temp = [f"{number:.{checkall}f}" for number in list]
    result = []
    for num in temp:
        if num[-1]=='0':
            result.append(num[:-1])
        else : 
            result.append(num)
    if step ==0.45:
        return "("+", ".join(result)+")"
    else :
        return "("+", ".join(temp)+")"
print("*** New Range ***")
number = [ float(x) for x in input("Enter Input : ").split(" ")]

if len(number)==1:
    print(range(number[0]))
elif len(number)==2:
    print(range(number[0],number[1]))
elif len(number)==3:
    print(range(number[0],number[1],number[2]))
