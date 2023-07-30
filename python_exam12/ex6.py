print(" *** Divisible number ***")
posnum = int(input("Enter a positive number : "))
numlist = []
if(posnum == 1):
    numlist.append(1)
for i in range(1,posnum):
    if (posnum%i == 0 )and i not in numlist:
        numlist.append(i)
        numlist.append(posnum//i)
    else: continue
numlist.sort()
count = len(numlist)
numlist = list(map(str,numlist))
if numlist ==[] : print ("0 is OUT of range !!!")
else :
    print("Output ==> "+" ".join(numlist))
    print("Total ==> "+ str(count))
