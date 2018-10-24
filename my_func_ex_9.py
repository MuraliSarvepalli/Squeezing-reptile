#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(*args):
    if sum(args)<=21:
        return sum(args)
    elif sum(args)>21 and 11 in args:
        s=sum(args)-10
        return s
    elif sum(args)>21:
        return 'BUST'
res=blackjack(5,6,7)
print(res)
    
