print("Welcome to FLAMES matching")
name1=input('Enter the name1')
name2=input('Enter the name2')
name1=list(name1)
name2=list(name2)
name=list(name1+name2)
for i in name:
    if i==' ':
        continue
    if i in name1 and i in name2:
        name1.remove(i)
        name2.remove(i)
        name.remove(i)
        name.remove(i)
a=len(name)
f=['f','l','a','m','e','s']
dic={'f':'Friends','l':'Lovers','a':'Affectionate','m':'Marriage','e':'enemies','s':'Siblings'}
while True:
    if len(f)==1:
        break
    d=a%len(f)
    f.pop(d-1)
    r=f[0:d-1]
    del f[0:d-1]
    f=f+r
    if len(f)==1:
        break
print("Your relationshio is {}".format(dic[f[0]]))
