#Write a Python function to check whether a string is pangram or not

import string
def panagram(st):
    for i in string.ascii_lowercase:
        if i in st:
            flag=1
        else:
            flag=0
    if flag==1:
        return True
    else:
        return False

st=input('Enter the sentence')
print(panagram(st))
