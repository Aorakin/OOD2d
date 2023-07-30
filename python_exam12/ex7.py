def changeposr(message : str,pos : int) :
    return message[-pos:]+message[:-pos]
def changeposl(message : str,pos : int) :
    return message[pos:]+message[:pos]
print("*** String Rotation ***")
mes = input("Enter 2 strings : ").split(' ')
message1= mes[0]
message2 = mes[1]
check = True
count=0
while check :
    if(changeposr(message1,2)== mes[0]and changeposl(message2,3)== mes[1] and count !=0):
        check = False
    message1=changeposr(message1,2)
    message2=changeposl(message2,3)
    count+=1
    if count <=5 :
        print(f'{count} {message1} {message2}')
    elif check==False and count >5:
        print(" . . . . . ")
        print(f'{count} {message1} {message2}')
    if check == False :
        print(f'Total of  {count} rounds.')