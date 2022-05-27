# multiple array in one big array
#from numpy import *
#arr1=array([
 #             [1,2,3,4,5,12],
  #            [6,7,8,9,1,45]



    #       ])

#for finding dimension of an array
#print(ndim(arr1))
# we can also find rows and columns by using (shape) function
#print(shape(arr1)) # the ist digit in output represent (rows) and the second represent the (columns)
#also find a size see the below example size means how many elements or no in the given arrays
#print(arr1.size)

#print(arr1)
# we can also convert multy dimensional array into a single dimensional array
#arr2=arr1.flatten()
# we can also make a multy dimension array from single dimensional array
#arr3=arr2.reshape(3,4)
#print(arr3)
# also make a two dimensional array from big three dimensional array so in the example below we make a two dimensional array from big three dimensional array also we make a single dimensional array
#arr3=arr2.reshape(2,2,3) # in the output each have two (D) arrays
# print(arr3)
#print(ndim(arr3))
# convert array into a amtrix
#m=matrix(arr1)
#print(m)
# we can also write it in the form of
#m=matrix('1,2,3;4,5,6')
#print(m)
# we can also find a diagonal of the matrices
#m=matrix('1 2 3;4 5 6;6 7 8')
#print(diagonal(m))

# we can also find (min) and (maximum) number in the given array
#m=matrix('1 2 3;4 5 6;6 7 8')
#print(m.max())
#m=matrix('1 2 3;4 5 6;6 7 8')
#print(m.min())
# how to multiply two matrics in short way (if the ist matrics row are equal to the 2nd matrics column then the matrices are conformable for multiplication)
#m1=matrix('1 2 3;4 5 6;6 7 8')
#m2=matrix('1 2 3;4 5 6;6 7 8')
#m=matrix('1 2 3;4 5 6;6 7 8')
#m3=m1*m2
#print(m3)
#by using numpy we use a dot() function it take two arguments and return the products
import numpy as np
# two dimensional arrays
m1 = np.array([[1,4,7],[2,5,8]])
m2 = np.array([[1,4],[2,5],[3,6]])
m3 = np.dot(m1,m2)
print(m3)

# three dimensional arrays
m1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
m2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])
m3 = np.dot(m1,m2)
print(m3)

