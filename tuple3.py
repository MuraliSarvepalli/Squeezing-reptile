d={'murali':2,'abinaya':3,'sriram':12,'ganesh':8,'ramki':4}
l=list()
m=list()
for i,j in list(d.items()):
    l.append((j,i))
print (l)
l.sort(reverse=True)
print (l)
for i,j in l:
    m.append((j,i))
print (m)
