# due to operator overloading we cannot add sub multiply divide 2 no we need a special method like add mul(for multiplication) and sub(for subtraction)etc

#class Employee:
 #   def __init__(self,name,sallary,role):
  #      self.name=name
  #      self.sallary=sallary
  #      self.role=role

  #  def printdetail(self):
  #      return f"the name is {self.name} the sallary is {self.sallary},the role is {self.role}"

  #  def __add__(self, other):
  #      return self.name+other.name


#emp1=Employee("ismail\n",456,"student\n")
#emp2=Employee("raheem",346,"student")

#print(emp1+emp2)

#class Student:
 #   def __init__(self,name,rollno):
  #      self.name=name
   #     self.rollno=rollno




#class Student2:
 #   def __init__(self,name,rollno):
  #      self.name=name
  #      self.rollno=rollno

    #def __add__(self, other):
    #    return self.rollno+other.rollno


    #def __truediv__(self, other):
     #   return self.rollno / other.rollno    #Operator Overloading means giving extended meaning beyond their predefined operational meaning.

                                               #means if it is string using operator plus the plus is overloadf on it and give sum of this two string see in the above example


#S1=Student("ismail\n",144)
#S2=Student("raheem",145)
#print(S1/S2)
a=15
if((a>2) and (a>10)) or (a>17 or a>18):
    print(1)
else:
    print(2)


