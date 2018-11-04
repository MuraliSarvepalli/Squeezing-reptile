#Write a Python function to multiply all the numbers in a list.

def multiply(lst):
    mul=1
    for i in lst:
        mul=i*mul
    return mul

lst=[1,2,3,4]
res=multiply(lst)
print(res)
