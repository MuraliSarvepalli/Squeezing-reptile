class murali:
    x=0
    def __init__(self):
        print('party begins')
    def party(self):
        self.x=self.x+1
        print("so far",self.x)

    def __del__(self):
        print("party ends")

p=murali()
print (type(p))
p.party()
murali.party(p)
p.party()
p=50
print(type(p))
