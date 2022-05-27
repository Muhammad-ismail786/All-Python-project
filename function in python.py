#def greet(): # this is the function definition
 #   print("hello")
 #   print("good morning")
#greet() # this is the function call
#def add(x,y):
 #   c=x+y
 #   print(c)
#add(4,5) # we can only call the function and insert a value to it
#greet()
#for return a value we can do it by another way
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(4,5)
print(result1,result2)



