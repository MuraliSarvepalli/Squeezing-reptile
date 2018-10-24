#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy(lst):
    if 0 in lst:
        a=lst.index(0)
        if 0 in lst[a+1:] and 7 in lst[a+1:]:
            if  lst[a+1:].index(0)<lst[a:].index(7):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
lst=[1,2,4,0,0,7,5]
r=spy(lst)
print(r)
