print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))
result = 0
while num>=10:
    result +=(num%10)
    num = num//10  
result += num
print(f'Summation of each digit =  {result}')