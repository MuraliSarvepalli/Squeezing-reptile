txt='but soft what light in yonder window breaks'
words=txt.split()
t=list()
for word in words:
    t.append((len(word),word))
print (t)
t.sort(reverse=True)
print (t)
res=[]
for i,j in t:
    res.append(j)
print (res)
    
