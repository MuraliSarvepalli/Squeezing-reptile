fhand=open('romeo.txt')
lst=[]
for line in fhand:
    words=line.split()
    for i in range(0,len(words)):
        if words[i] in lst:
            continue
        lst.append(words[i])
        lst.sort()
    

print (lst)
