#class
class Dog():
    def bark(self,number):# this is a class methoddefined
        print("woof,My name is {} and number is{} and species is {}".format(self.name,number,self.species))
    species='mammal'#this is a class obj attribute, can be called when evr an instance is created
    def __init__(self,breed,name,spots):#this is a constructor function,applies to that particular instance of class#invoked whenan obj is createed
        self.breed=breed
        self.name=name
        self.spots=spots

mydog=Dog('lab','jimmy',False)
print(mydog.breed,mydog.name,mydog.spots)
print(mydog.species)
print(mydog.bark(20))



# if we are going to use the class atributes inside a method of a class, we need use it with self--(name,breed,species,spots)
# it it is an argument , we need not use self--ex(number)
