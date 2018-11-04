class Cylinder:
    pi=3.14 
    def __init__(self,height=1,radius=1):
        self.hgt=height
        self.rad=radius
        
    def volume(self):
        return self.pi*self.rad*self.rad*self.hgt
    
    def surface_area(self):
        return 2*self.pi*self.rad*(self.hgt+self.rad)


c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
