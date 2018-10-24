 #Given a string, return a string where for every character in the original there are three characters

def my_func(word):
    lst=[]
    for i in word:
        lst.append(i*3)
    s=''.join(lst)
    return s

word=input('Enter the name')
res=my_func(word)
print(res)
    
        
