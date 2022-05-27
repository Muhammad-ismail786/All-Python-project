#class A:

 #   def __init__(self):
 #            print("this is A")
 #   def feature1(self):



   #  def feature2(self):
  #             print("this is features 2")

#class B(A):
 #   def __init__(self):
 #       super().__init__() # we call the init method/function of class A
  #      print("this is B")

  #  def feature3(self):
   #       print("this is features 3")
    #def feature4(self):
     #          print("this is features 4")



#a=B()

# (MRO) method resolution order
class A:

     def __init__(self):
         print("this is A")
     def feature1(self):
         print("this is feature 1")



     def feature2(self):
               print("this is features 2")

class B:
    def __init__(self):
     #   super().__init__() # we call the init method/function of class A
        print("this is B")

    def feature3(self):
          print("this is features 3")
    def feature4(self):
               print("this is features 4")

class C(A,B):
    def __init__(self):
        super().__init__()
        # it print iniit method/function (A) and (C)  because its follow the rule from left do right bcz of (MRO))

        print("this is C")
    def feat(self):
        super().feature2()

a=C()
a.feat()


# the output is (this is A) and (this is C)

# also same for the method see in the example below
a.feature1()
# the output will be (this is feature 1) bcz of (MRO) method resolution order

# here we learn three thing
# no 1:how constructor behaves in inheritance
# no 2:how to use super() in inheritance
# no 3:(MRO) method resolution order (left to right order)

# we can call other method by using super() method or function
# see in the example above at line no (55)

