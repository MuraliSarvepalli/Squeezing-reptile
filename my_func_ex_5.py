#return the sentence with the words reversed
def word_reverse(sentence):
    lst=[]
    lst=sentence.split()
    lst1=lst[::-1]
    s=' '.join(lst1)
    return s
sentence=input('Enter the sentence')
r=word_reverse(sentence)
print(r)
