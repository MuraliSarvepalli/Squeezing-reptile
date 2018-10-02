import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]=counts[word]+1
print (counts)

