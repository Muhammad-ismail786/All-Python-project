# poly means many morph mean shape/form one thing having many shape is called polymorphism

# duck typing in python
# if there is a birds which walk like a duck which swim like a duck which sleep like a duck then this is duck no matter which type of birds is it but whose character/behaviour like a duck then this is duck

# Attributes having same name are
# considered as duck typing


# Python program to demonstrate
# duck typing


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")

object=Bird()
object.fly()
#for object in Bird(),Airplane(),Fish():
 #   object.fly()

#b=Bird()
#b.fly()
#a=Airplane()
#a.fly()
#c=Fish()
#c.swim()