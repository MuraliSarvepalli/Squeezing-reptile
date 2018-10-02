fhand=open('words.txt')
word_dict = dict()
for line in fhand:
        word = line.strip()
        word_dict[word] = word
print (word_dict)
