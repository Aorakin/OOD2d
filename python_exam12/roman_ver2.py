class MyInt():
    def __init__(self, value) :
        self.value = value
    def toRoman(self):
        intNroman = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40 ,"X": 10,"IX":9,"V": 5,"IV":4,"I": 1,}
        val = self.value
        result = []
        for i,j in intNroman.items():
            if val //j != 0:
                result.append(i*(val//j))
                val -= j*(val//j)
        return "".join(result)
    def __add__(self,number):
        return int((self.value + number.value)*1.5)
print(" *** class MyInt ***")
num1,num2 = input("Enter 2 number : ").split(" ")
num1 = MyInt(int(num1))
num2 = MyInt(int(num2))
print("{0} convert to Roman : {1}".format(num1.value,num1.toRoman()))
print("{0} convert to Roman : {1}".format(num2.value,num2.toRoman()))
print("{0} + {1} = {2}".format(num1.value,num2.value,num1+num2))