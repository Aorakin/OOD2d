print("*** multiplication or sum ***")
num = input("Enter num1 num2 : ")
lt = list(map(int,num.split(" ")))
if lt[0]*lt[1]>1000:
    print("The result is "+str(lt[0]+lt[1]))
else :
    print("The result is "+str(lt[0]*lt[1]))