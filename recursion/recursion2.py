# def firststring(string,num):
#     if num == 0:
#         return string[num]
#     elif num < len(string)/2:
#         return firststring(string,num-1)+string[num]
#     else :
#         return firststring(string,num-1)

# def sec(string,num):
#     if  num == len(string)-1:
#         return string[num]
#     else:
#         return sec(string,num+1) + string[num]
# inp = input("Enter Input : ")
# length = len(inp)

# if (firststring(inp,length//2)) == (sec(inp,length//2)):
#     print("'{0}' is palindrome".format(inp))
# else:
#     print("'{0}' is not palindrome".format(inp))
string = input("enter : ")
def parindrome(num):
    global string
    if num >= (int(len(string)/2))-1:
        return True
    if string[num] != string[-(num+1)]:
        return False
    return parindrome(num+1)
print(parindrome(0))