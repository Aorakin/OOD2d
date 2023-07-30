print("*** Rabbit & Turtle ***")
val = input("Enter Input : ")
lt = list(map(float,val.split(' ')))
time = lt[0]/(lt[2]-lt[1])
fdistance = lt[3]*time 
print("%.2f"%fdistance)

