
pos=-1

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:

           if list[mid]<=n:
            l=mid+1
           else:
                u=mid-1
                return False


list=[1,4,8,7,6,3,2,78,86,96,94,12,45]
n=10
if search(list,n):
    print("found at position:",pos+1)

else:
    print("not found")


