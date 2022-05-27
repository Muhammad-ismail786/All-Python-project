# variable
# there are two types of variable (instance variable )and other one is(class or static variable)
#instance variable=the variable which is declared inside the init or(object) is called.....
#class variable=the variable which is declared inside the class is called....


# namespace=namespace is an area where you create and store object/variable
# there are two namespace (class namespace) and object/instance namespace
#class namespace where we store the class variable
#instance/object namespace where we store object variable

#jab aik object ma ham function ko call karanga tho self automatically waha jayega (matlab self ma jetnay wariable ha wo khood ba khood run hoga
class Employee:
    # if we write here something then this is called (class variable)
  #  student=12
    def __init__(self):
         self.sallary=25000
         self.name="rohan"
         self.address="wana"

c1=Employee()
c2=Employee()
c3=Employee()
student=Employee
print('the sallary is:',c1.sallary, '\nthe name is:',c2.name,'\nhe belong to:',c3.address)


