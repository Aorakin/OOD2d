class MyInt():
    def __init__(self,val):
        self.val = val
    def toRoman(self) :
        roman = ["I","V","X","L","C","D","M"]
        integer = [1,5,10,50,100,500,1000,1]
        value = self.val
        check = 0
        resultList = []
        result=""
        while value >0:
            num = (value%10)*(10**check)
            while num!=0:
                if num // integer[check*2+1]==1 and num-integer[check*2+1]<=3*(10**check):      
                    num -=integer[check*2+1]
                    resultList.append(roman[check*2]*(num//integer[check*2]))
                    resultList.append(roman[check*2+1])
                    # print(integer[check*2]*(num//integer[check*2]))
                    # num= num - integer[check*2]*(num//integer[check*2])
                elif num-integer[check*2+1]==4*(10**check):
                    resultList.append(roman[check*2]+roman[check*2+2])
                    # num-=integer[check*2+1]+4*(10**check)
                elif num==4*(10**check):
                    resultList.append(roman[check*2]+roman[check*2+1])
                    # num-= 4*(10**check)
                else:
                    resultList.append(roman[check*2]*(num//integer[check*2]))
                    # num-=integer[check*2]*(num%5)
                num = 0
            if check<3:
                check+=1
            value = value//10
        for i in range (len(resultList)):
            result+="".join(resultList[-(i+1)])
        return result
    def __add__(self,number):
        return int((self.val + number.val)*1.5)
print(" *** class MyInt ***")  
num1,num2 = input("Enter 2 number : ").split(" ")
num1 = MyInt(int(num1))
num2 = MyInt(int(num2))
print("{0} convert to Roman : {1}".format(num1.val,num1.toRoman()))
print("{0} convert to Roman : {1}".format(num2.val,num2.toRoman()))
print("{0} + {1} = {2}".format(num1.val,num2.val,num1+num2))
