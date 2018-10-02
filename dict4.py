fhand=open('romeo.txt')
d=dict()
for line in fhand:
    words=line.split()
    words.sort()
    for i in words:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1

print (d)
for i in d:
    if d[i]>1:
        print (i,d[i])
