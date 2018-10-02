import re
count=0
a='murali krishna'
for i in a:
    if re.findall('[aeiou]',i):
        count=count+1
print (count)
