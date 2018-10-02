import string
fhand=open('romeo-full.txt')
d=dict()
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    words.sort()
    for i in words:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
print (d)
b=list(d.keys())
print (b)
b.sort()
for key in b:
    if d[key]>1:
        print (key,d[key])
