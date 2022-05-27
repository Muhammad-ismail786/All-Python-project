class student:
# class method that defined inside the class
    school='iqra'

    def __init__(self,m1,m2,m3):
        self.m1=m1   #(m1,m2,m3 all are instance)
        self.m2=m2
        self.m3=m3

    def get_m1(self): #its only fetch the value called accessor   (instance method two in metod that belong to instance (mutator) and (accessor)
        return self.m1

    def set_m1(self): # only modified a value called mutator        (instance method)
        return self.m1

    def avg(self): # instance method bcz its word with object (there are two types of method (mutator) and (accessor)
       return(self.m1+self.m2+self.m3)/3

    #def info(self): # if we word with instance we use the (self) but if we work with class we use the (cls) keyword
    @classmethod
    def info(cls):   # class method
     return cls.school

# (static metod) a method that do not work with class and instance or object is called static method
# using a decorator called staticmethod decorator
    @staticmethod
    def info():
        print("this is the class of student")
#student.info()

#s1=student(23,45,67)
#s2=student(34,65,76)
#print(s1.avg())
print(student.info())
