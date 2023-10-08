def drawing(n,maxn):
    if n==1:
        return "*" 
    first = n*"*"
    if len(first)!= maxn:
        first +=" "*(maxn-n)
    print(first)
    return drawing(n-1,maxn)

print(drawing(3,3))