def binarynum(num,Mpos):
    if num < 2**Mpos-1:
        print(bi((num),Mpos-1))
        return binarynum((num+1),Mpos)
    else:
        return (bi((num),Mpos-1))
        
def bi(num,e):
    if e==0 or e<0:
        return str(num)
    elif num//(2**e) ==0 or num//(2**e) == 1:
        return str(num//(2**e))+bi(num%(2**e),e-1)
    else:
        print("check")
inp = int(input("Enter Number : "))
if inp < 0 :
    print("Only Positive & Zero Number ! ! !")
else:
    print(binarynum(0,inp))