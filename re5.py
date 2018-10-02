import re
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    lst= re.findall('^X\S*: ([0-9.]+)',line)
    if len(lst)>0:
        print (lst)
