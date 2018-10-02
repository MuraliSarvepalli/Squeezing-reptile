import re
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('^F..m:.+@',line):
        print (line)
