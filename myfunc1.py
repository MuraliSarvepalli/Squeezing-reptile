def myfunc(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    else:
        if a>b:
            return a
        else:
            return b
res=myfunc(2,6)
print(res)
