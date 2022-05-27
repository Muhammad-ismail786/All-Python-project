# (method overloading) when there are 2 method/function and take a different argument this is called method overloading
# (method overriding) when 2 method/function having the same name and perform a different task and having the same parameter
# we cannot o method overloading in python directlly we can use the method given below

# this is (method overloading)
#class student:
 #   def __init__(self,m1,m2):
 #       self.m1=m1
 #       self.m2=m2



   # def sum(self,a,b,):

        # if we pass three arguments its does not work for solving this problem we can use a key word (none)
  #  def sum(self, a=None, b=None,c=None ):
   #     s=0
   #     if a!=None and b!=None and c!=None:


    #        s=a+b+c
    #    elif a!=None and b!=None:
     #       s=a+b
     #   else:
     #       s=a

     #   return s

#s=student(4,5)
#print(s.sum(4,6))


# here we can do (method overridding)
# see below
# in method overridding we can use the concept of inheritance
class A:
    def Amin(self):
        print("hello amin bhai")


#class B(A):
    # here we can inherate (A) into (B) to solve the problem of (method overridding)
    # if ther are something in the (B) class then ist execute it see in the example
class B(A):
    def show(self):
        print("i m in the class")


#a1=A()
#a1.Amin()
a1=B()
# it gives an error bcz (B) object has no attributes amin (for solving this problem we can take help from (inheritance) by inheritate (A into B)
a1.show()
# if you call (show) it will call the show method  of the sub class

