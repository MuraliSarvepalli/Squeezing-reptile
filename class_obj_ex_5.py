#find distance and slope of the line
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
       d=((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)
       return d**0.5
    
    def slope(self):
        m=(self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        return m
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
