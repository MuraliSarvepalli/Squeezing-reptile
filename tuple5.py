d={('murali','accenture'):2,('sairam','caterpillar'):2.5,('ashok','collabera'):8,('harika','IBM'):1}
l=list()
m=list()
for i,j in list(d.items()):
    l.append((j,i))

l.sort(reverse=True)
print (l)

for i,j in l:
    m.append((j,i))
print (m)


