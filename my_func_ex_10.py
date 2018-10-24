#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers+


def summer(lst):
    count=0
    s=0
    while count<len(lst):
        if lst[count]==6:
            for i in range(count,lst.index(9)):
                count=count+1
        else:
            s=s+lst[count]
        count+=1
    return s

a=summer([6,7,9,13])
print(a)
                
