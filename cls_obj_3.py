class person:
    x=0
    def __init__(self,nam):
        self.name=nam
        print(self.name,'party begins')
    def party(self):
        self.x=self.x+1
        print(self.name,'party count',self.x)

a=person('murali')
b=person('ashok')

a.party()
b.party()
a.party()
b.party()
a.party()
