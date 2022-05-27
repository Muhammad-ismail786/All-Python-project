# filter are given the sequence of a number
#nums=[2,3,4,5,6,7]
#even=list(filter(lambda n:n%2==0,nums))
#print(even)

# (MAPS) is used to double the value


#ums = [2, 3, 4, 5, 6, 7]
#evens = list(filter(lambda n: n % 2 == 0, nums))
#doubles = list(map(lambda n: n * 2, evens))
#print(doubles)

# reduce is used to add all the value for adding we want to parameters
from functools import reduce
def Add_All(a,b):
    return a+b

nums=[2,3,4,5,6,7]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
print(doubles)
sum=reduce(Add_All,doubles)