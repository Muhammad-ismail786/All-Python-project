# if u want to pass multiple data with the help of keyword then we have to use keyword (variable length) arguments and use a double star(**) in the function definition during pass an arguments
#def person(name,**data):# here we use a double star for multiple data
 #   print(name)
 #   print(data)
#person('navin',age=25,city='wana',mob=965123567)

# we can also use a for loop
def person(name,**data):# here we use a double star for multiple data
    print(name)
    for i,j in data.items():
        print(i,j)

   # print(data)
person('navin',age=25,city='wana',mob=965123567)