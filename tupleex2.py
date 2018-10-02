import string
fhand=open('mbox-short.txt')
count={}
lst=[]
hr=[]
l=list()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        print (line)
        words=line.split()
        lst.append(words[5])
        
for i in range(0,len(lst)-1):
    t=lst[i]
    h=t.split(':')
    hr.append(h[0])

for i in hr:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1
print (count)


for i,j in (count.items()):
    l.append((i,j))

l.sort()

for i,j in l:
    print (i,j)
