def right_shift (num : int, shift : int) :
    print(num>> shift)
number = [int(i) for i in input("Enter number and shiftcount : ").split()]
right_shift(number[0],number[1])