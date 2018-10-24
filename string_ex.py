def myfunc(st):
    count=0
    s=[]
    for item in st:
        if count%2==0:
            s.append(item.lower())
        if count%2!=0:
            s.append(item.upper())
        count=count+1
    print(s)
    str1=''.join(s)
    return str1
a=myfunc('MuraLi')
print(a)
