# in Unsigned character or integer you dont enter a (negative number) and unsigned char is represented by big letter like(A,B,C,D etc)
# in a signed you can enter any type of value negative or +ve and represented by small alphabet(a,b,c,d,e....)
from array import *
#vals=array('i',[2,4,6,7,9,3])
#for i in range(5):

  #  print(vals[i])
#vals=array('i',[2,4,6,7,9,3])
#for e in vals:
 #   print(e)# here (e) fetch the value one by one
  #  print(vals[i])
#vals=array('u',['a','e','i','o','u'])
#for e in vals:
 #   print(e)
#vals=array('i',[1,2,3,4,5,6])
#newArr=array(vals.typecode,(a for a in vals))
#for e in newArr:
 #   print(e)
 #for squaring of a number
#vals=array('i',[1,2,3,4,5,6])
#newArr=array(vals.typecode,(a*a for a in vals))
#for e in newArr:
 #   print(e)
 # we can also use a (while loop)
vals=array('i',[1,2,3,4,5,6])
newArr=array(vals.typecode,(a*a for a in vals))
i=0 #initialization
while i<len(newArr):
    print(newArr[i])
    i+=1 #increment also we can decrement it