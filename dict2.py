word=input("enter the name")
d=dict()
for i in word:
    d[i]=d.get(i,0)+1
print (d)
