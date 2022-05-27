#def update (x):
  #  x=8
  #  print("x",x)
  #  print(id(x))
#a=10
#update(a) # here we pass a value (10) not a # this is called pass by value both value 8 and 10 having same address or pointing the same address
#print(id(a))
#print("a",a)
# when ever you call a function by passing a avalue to a function they will share the same id or address
#but when you change the value its change the address
def update (x):

    print(id(x))
    x = 10
    print(id(x))

    print("x", x)
a=7

print(id(a))
update(a)
print("a",a)