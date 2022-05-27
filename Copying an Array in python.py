#vectorized operaration in array by additng two array
from numpy import *
arr2=array([6,7,8,9,3])
#arr3=arr1+arr2
#print(arr3)
#we can find alot of value here like (max) (min) sin cose etc
arr1=array([1,2,3,4,5])
#print(max(arr1))
#print(min(arr1))
#print(sin(arr1))
#print(cos(arr1))   #there are also alot of function here to solve              imp: using the same address for the same value in a memory is called (aliasing)
# writentwo array in a sequence using a function concatenate

#print(concatenate([arr1,arr2]))
# array of the same address
#arr1=array([12,3,456,67])
#arr2=array([23,45,67,89,12])
#arr1=arr2


#print(arr1)
#print(arr2)
#print(id(arr2))
# here is also use a function called view which give the different address or new address in a memory for the same value
#arr1=array([12,3,456,67])
#arr2=arr1.view()

#this hving different address
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))

# this is called (shallow copy) when we change a value in real array the value also change in its copy array
#arr1[2]=200
#arr1=array([12,3,456,67])
#arr2=array([23,45,67,89,12])
#arr2=arr1.view()
#arr1[2]=7
#print((arr1))
#print((arr2))
#print(id(arr1))
#print(id(arr2))



# there is also another type of copy is (Deep copy) in which there is no change occurs in original array but only its copy array value change when u want to change it see in the examole below
# here also use a function called (copy)

arr1[2]=200
arr1=array([12,3,456,67])
#arr2=array([23,45,67,89,12])
arr2=arr1.copy()
arr1[2]=7
print((arr1))
print((arr2))
print(id(arr1))
print(id(arr2))