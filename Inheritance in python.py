# when the behaviour/property of one class will be inherited or transfer to another class is called inheritance
# the ist class is called (parent class) and the class which take the property from parent class is called (child or derived class)


# this is called single level inheritance
#class A:
#    def feature1(self):
 #       print("this is features 1")


  #  def feature2(self):
  #      print("this is features 2")

#class B(A): # it means all the features of (A) will assigned/transfered to (B) this is called inheritance

 #           def feature3(self):
 #               print("this is features 3")
 #           def feature4(self):
  #              print("this is features 4")


#a1=B(A)
#a1.feature1()
#a1.feature2()
#b=B()
#b.features3()
#b.features4()
#b1=B()
#b1.feature1()

# also for same for (A)
#a1=A()
#a1.feature1()
#a1.feature2()



# multi_level inheritance which is the child of class (B) and whose grand father is class (A)
class A:
     def feature1(self):
        print("this is features 1")


     def feature2(self):
        print("this is features 2")

class B(A): # it means all the features of (A) will assigned/transfered to (B) this is called inheritance

     def feature3(self):
              print("this is features 3")
     def feature4(self):
              print("this is features 4")


class C(A,B):
    # (for multiple level) we put both (A) and (B) in (C)
    def feature5(self):
            print("this is features 5")



#a1=A()
#a1.feature1()
#a1.feature2()

b1=B()
#b1.feature4()
#b1.feature3()
C=C()

C.feature1()

# (multiple inheritance) when one class inherit the both class here (c) inherit both (A) and (B)
# for this we can put both (A) and (B) in (C)
