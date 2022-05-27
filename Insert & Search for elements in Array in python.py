from array import *
arr=array('i',[])
n=int(input("enter the length you want:"))
for i in range(n):
    x=int(input("enter the next value :"))
    arr.append(x)


print(arr)
val=int(input("enter the value for search:"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    K=k+1
    # also use the function by finding indexing
print(arr.index(val))