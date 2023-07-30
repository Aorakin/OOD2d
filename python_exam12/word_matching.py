print("*** TorKham HanSaa ***")
word = input("Enter Input : ").split(",")
result = []
for mes in range (len(word)) :
    checkmessage = word[mes].split(" ")
    if len(checkmessage) == 2:
        if not result and checkmessage[0] == 'P':
            result.append(checkmessage[1])
            print(f'\'{checkmessage[1]}\' -> {result}')
        elif checkmessage[0] == 'P' and checkmessage[1][:2].upper() == result[-1][-2:].upper() :
            result.append(checkmessage[1])
            print(f'\'{checkmessage[1]}\' -> {result}') 
        elif checkmessage[0].islower():
            print(f'\'{word[mes]}\' is Invalid Input !!!')
            break
        else :
            print(f'\'{checkmessage[1]}\' -> game over')
            break
    elif len(checkmessage) ==1:
        if checkmessage[0].islower():
            print("Invalid Input !!!")
        elif checkmessage[0] == "R":
            print("game restarted")
            result = []
        elif checkmessage[0] == "X":
            break