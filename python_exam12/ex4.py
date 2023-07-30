print(" *** Wind classification ***")
swind = float(input("Enter wind speed (km/h) : "))
if swind <0:
    print("!!!Wrong value can't classify.")
elif swind>=0 and swind<52 :
    print("Wind classification is Breeze.")
elif swind>=52 and swind<56:
    print("Wind classification is Depression.")
elif swind>=56 and swind<102:
    print("Wind classification is Tropical Storm.")
elif swind>=102 and swind<209:
    print("Wind classification is Typhoon.")
else : print("Wind classification is Super Typhoon.")