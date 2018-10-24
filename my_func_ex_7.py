#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere

def three_conseq(ls):
    count=0
    while count<len(ls):
        if ls[count]==3 and ls[count+1]==3:
            return True
        count+=1
ls=[]
for i in range(0,5):
    num=int(input('Enter the values'))
    ls.append(num)
print(ls)    
r=three_conseq(ls)
print(r)
