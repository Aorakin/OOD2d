def checkIso(string1,string2):
    if len(string1) != len(string2):
        return False
    templist = []
    templist_string1 = []
    for i in range(len(string1)):
        if templist and string1[i] in templist_string1 and string2[i]!= templist[templist_string1.index(string1[i])] :
            return False
        elif not templist or(templist and(string2[i] not in templist )) or (string1[templist.index(string2[i])] == string1[i])  :
            templist_string1.append(string1[i])
            templist.append(string2[i])
        else:
            return False
    return True


inp = input("Enter str1,str2: ").split(",")
notHave = " not"
if checkIso(inp[0],inp[1]):
    notHave = ''
print(f"{inp[0]} and {inp[1]} are{notHave} Isomorphic")