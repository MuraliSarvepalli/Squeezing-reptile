import re
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('^X\S*: ([0-9.]+)',line):
        print(line)
