# we do not access the inner class we make the object of outer class then we can access the inner class

class College:
    def __init__(self):
        print("college is the outer class")

    class Student:
        def __init__(self):
            print("student is the inner class")
        def displayS(self):
            print("student method")

    def displayC(self):
            print("college method")



C=College()
C.displayC()
#s.displays()  # we cannot display the inner look we can make the object of outer class in inner class the we can run it see in the below example
#S=c.student()
#S.displays()

# we cannot access direct the outer class same as the above we can access the outer class in inner class by using the inner class object and mention the outer class name
#s=college().student()
#s.displays()
#we cannot create the student class direct we use the outer class object to create the inner class object
#S=C.Student()
#S.displayS()
S=College().Student()
S.displayS()

