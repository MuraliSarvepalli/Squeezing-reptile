from cls_obj_3 import person
class cricket(person):
    points=0
    def six(self):
        self.points=self.points+6
        self.party()
        print(self.name,"points",self.points)

a=person('murali')
a.party()
b=cricket('ashok')
b.party()
b.six()
