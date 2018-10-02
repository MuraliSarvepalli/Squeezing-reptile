import re
fhand=open('mbox.txt')
sum=0
count=0
for line in fhand:
    line=line.rstrip()
    x=re.findall(r'New\s\S+:\s([0-9.]+)',line)
    if len(x)>0:
        sum=sum+int(x[0])
        count=count+1

average=sum/count
print (average)

