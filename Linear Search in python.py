
pos=-1
def search(list,n):
     i=0
     while i<len(list):

  #   for i in range(6): we can also use a for loop but while is better bcz we can increase and decrease the lenth anytime

         if list[i]==n:

             globals()['pos']=i

             return True
         i=i+1
     return False



list=[1,4,8,7,6,3,2]
n=7
if search(list,n):
    print("found at position:",pos)

else:
    print("not found")



