def permute_string(string,k):
    if k < 0 :
        return 1
    elif k > len(string):
        return 2
    elif k == 0 :
        return [""]
    else :
        return generate_permutations(string,k,"",0)
    
def generate_permutations(string,k,pick,index):
    if len(pick) == k:
        return [pick]
    elif index >= len(string):
        return []
    else : 
        permute1 = generate_permutations(string[:index]+string[index+1:],k,pick+string[index],0)
        permute2 = generate_permutations(string,k,pick,index+1)    
    return permute1 + permute2

inp = input("Enter a string and k: ").split("/")
result = permute_string(inp[0],int(inp[1]))
if result == 1:
    print("Invalid value of k. k must be a non-negative integer.")
elif result == 2 :
    print("Invalid value of k. k must be less than or equal to the length of the string.")
else:
    result = list(set(result))
    result.sort()
    print(result)