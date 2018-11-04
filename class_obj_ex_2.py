class Circle():
    pi=3.14 # Class obj attribute

    def __init__(self,rad=1): # here we are initializing rad=1 (default_value) ,but it can be overridden if we pass some other value by calling using instance of object
        self.rad=rad
        self.area=rad*rad*self.pi

    def circum(self):
        return 2*self.pi*self.rad


cir=Circle(3)
print(cir.area)
print(cir.circum())


    
