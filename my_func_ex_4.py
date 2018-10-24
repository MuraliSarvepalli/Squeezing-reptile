#Capitalizes the first and fourth letter of a name
def capitalize_one_four(name):
    lst=[]
    count=0
    for i in name:
        lst.append(i)
        if count==1 or count==4:
            lst[count]=i.upper()
        count=count+1
    s=''.join(lst)
    return s
name=input('Enter the name')
r=capitalize_one_four(name)
print(r)
