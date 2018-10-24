# Given an integer n, return True if n is within 10 of either 100 or 200
def withinten(a):
    if abs(a-100)<=10 or abs(a-200)<=10:
        return True
    else:
        return False

a=input('enter the num')
r=withinten(int(a))
print(r)
