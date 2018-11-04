#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(mylist):
    un_list=set(mylist)
    return un_list

print(unique([1,1,1,1,3,3,5,4,9,5,6,7,8,7,2]))
