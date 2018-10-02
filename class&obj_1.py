class murali:
    x=0
    def murali_f(self):
        self.x=self.x+1
        print("so far",self.x)

a=murali()

a.murali_f()
a.murali_f()
murali.murali_f(a)
