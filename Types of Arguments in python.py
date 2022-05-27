#def  add(a,b):#we pass (a) and (b) and given no value to it this is called (formal) arguments
 #   c=a+b
  #  print(c)
#add(4,5) # here we pass the arguments or specific value this arguments is called (actual arguments)
# this (actual) arguments have four types (position) (keyword) (default) (variable length)
#def  person(name,age):
 #   print(name)
 #   print(age)


#person('gohar',25) # this is called position arguments whe the variable direct connect to the value here the gohar inter to the name arguments and 25 enter to the age arguments


# (keyword) arguments when mention the the keyword when enter the value this is called keyword arguments like see below
#def  person(name,age):
 #   print(name)
#    print(age)


#person(name='gohar',age=25)

# default arguments when you given a value in the upper function then by default the value is shown in the below function this is called default function
#def  person(name,age=16):
  #  print(name)
   # print(age)


#person(name='gohar') # in the result show 16 this is called default arguments when we give the value in the function it also print it like see below


#def  person(name,age=16):
 #   print(name)
  #  print(age)


#person(name='gohar',age=25)# here show in the result gohar 25 the upper age is default if there is no age mention in the below then by default he can gives us the value

 # the last is the (variable length arguments)
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
   # print(a)
    print(c)  # the first value assign to (a) all other value are enter to (b)

sum(2,4,5,6,7)

