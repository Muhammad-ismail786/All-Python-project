# the (variable) inside the function is called (local) variable
# and the (variable) outside the function is called (global) variable
#a=10
#def func():
 #   a=15
 #   print("in fun",a) # the preference always give a local variable

#func()
#print("hello world",a)


# we can also access a global variable inside a function by using the (global) keyword see below
#a=10
#def func():
 #   global a
 #   a=15
 #   print("in fun",a) # the preference always give a local variable
# here the (a) will be change to global variable by using the keyword (global)
#func()
#print("hello world",a)

# if we can print more then one value (global) value we can use a function globals
c=16
a=10
print(id(a))
def func():
    global a
    x=globals()['a']
    print(id(x))
    print("in fun",a) # the preference always give a local variable
# here the (a) will be change to global variable by using the keyword (global)
globals()['a']=12
func()
#print("hello world",a)