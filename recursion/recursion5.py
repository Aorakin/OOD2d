def Fac(num):
    if num == 0 :
        return 1
    else:
        return Fac(num-1)*num

def permute_string(string,k):
    if k < 0 :
        return "Invalid value of k. k must be a non-negative integer."
    elif k > len(string):
        return "Invalid value of k. k must be less than or equal to the length of the string."
    elif k == 0 :
        return [""]
    else :
        return generate_permutations(string,k,[])
    
def generate_permutations(string,k,newlist):
    length = len(newlist)
    string_size = len(string)
    Per =  Fac(string_size)//Fac(string_size-k)
    result = ""
    if length < Per:
        for i in range(length,k+length):
            result = result+string[i%string_size]
        newlist.append(result)
        return generate_permutations(string,k,newlist)
    else:
        newlist = list(set(newlist))
        newlist.sort()
        return newlist

inp = input("Enter a string and k: ").split("/")
print(permute_string(inp[0],int(inp[1])))
