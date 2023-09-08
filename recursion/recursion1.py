def print1ToN(n):
    if abs(n) == 1 or n <= 0 :
        return 1 
    return str(print1ToN(abs(n)-1))+" "+str(abs(n)) 
        
def printNto1(n):
    if n > 1:
        print(abs(n),end=" ")
        return printNto1(abs(n)-1)
    elif n == 0 or n <0 :
        return 1
    else: 
        return abs(n)

n = int(input("Enter Input : "))
print(print1ToN(n),end = " ")
print(printNto1(n))