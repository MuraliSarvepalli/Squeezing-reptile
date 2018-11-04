#vol of a sphere
def vol(r):
    v=float(4/3)*3.14*r*r*r
    return v

rad=float(input('enter the radius'))
print(vol(rad))
