import string
fhand=open('mbox-short.txt')
count={}
lst=[]
for line in fhand:
    line=line.rstrip()
    if line.startswith('From'):
        words=line.split()
        lst.append(words[1])

for i in lst:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1


l=list()
for i,j in (count.items()):
    l.append((j,i))

l.sort(reverse=True)

for i,j in l[:1]:
    print (j,i)
    


