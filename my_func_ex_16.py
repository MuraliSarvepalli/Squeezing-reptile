# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters

def up_low(sentence):
    count_up=0
    count_low=0
    for i in sentence:
        if i.isupper():
            count_up+=1
        elif i.islower():
            count_low+=1
        else:
            pass
    return print('count of uppercase is {}, count of lowercase is {}'.format(count_up,count_low))

sentence=input('enter the string')
up_low(sentence)
