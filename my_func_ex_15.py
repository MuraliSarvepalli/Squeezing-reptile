#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran(n,l,h):
    if n>=l and n<=h:
       return print('{} is in the range of {} and {}'.format(n,l,h))

n=int(input('Enter the number'))
l=int(input('Enter the lower range'))
h=int(input('Enter the higher range'))
ran(n,l,h)
