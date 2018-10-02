fhand=open('mbox-short.txt')
d=dict()
lst=[]
for line in fhand:
    lines=line.rstrip()
    if lines.startswith('From '):
        word=lines.split()
        print (word)
        lst.append(word[2])

for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
            
print (d)

