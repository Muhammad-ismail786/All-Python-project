#class topten:
 #   def __init__(self):
  #      self.num=1


 #   def __iter__(self):
 #       return self


 #   def __next__(self):
  #      if self.num<=10:
  #          val=self.num
   #         self.num+=1
    #        return val
     #   else:
      #      raise StopIteration



#values=topten()
#for i in values:
#    print(i)

# integer object is not iterable see below

#num=345
#for i in num:
 #   print(i)

 # string object is iterable

#num="345"
#for i in num:
 #   print(i)

# iterable is the object which give you an iterable
# iterator is an object in which the next object will be defined
#iteration

# for one by one printing character or integer we can also do like that

num="ismail"
#for i in num:

iter1=iter(num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))


