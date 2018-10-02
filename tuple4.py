import string
fhand=open('romeo-full.txt')
counts=dict()
for line in fhand:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    line=line.rstrip()
    words=line.split()
    for word in words:
        if word not in counts:
                        counts[word]=1
        else:
                        counts[word]=counts[word]+1

l=list()

for i,j in list(counts.items()):
    l.append((j,i))



l.sort(reverse=True)
for i,j in l[:10]:
    print (i,j)
    
