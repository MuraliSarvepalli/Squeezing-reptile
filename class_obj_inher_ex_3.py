#inheritance

class student():
    def __init__(self):
        print("Student Created")
    def work(self):
        print("I am working")
    def who_am_i(self):
        print("I am a student")

class boy(student):
    def __init__(self,name):
        student.__init__(self)  # using the student init
        print("Boy created")
        self.name=name
        print(self.name)

    def who_am_i(self):   #over ridden method 
        print("I am murali")
    def work(self):
        print("I am murali and i am working")
murali=boy('murali')
murali.work()   #overridden method
murali.who_am_i() #overridden method
