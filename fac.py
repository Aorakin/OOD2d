arr = {}

def dpfac(n):
    if n == 0 or n == 1:
        arr[0] = 1
        arr[1] = 1
    elif n not in arr.keys():
        arr[n] =  n * dpfac(n - 1)
    
    return arr[n]

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n-1)

print(f"{999}! =",dpfac(5))