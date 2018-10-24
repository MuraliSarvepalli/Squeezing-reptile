def myfunc3(a,b):
    if (a+b)==20 or a==20 or b==20:
        return True
    else:
        return False
x=input('Enter a')
y=input('Enter b')
r=myfunc3(int(x),int(y))
print(r)
