# there are three types of error
# compile time error # syntic error (syntatical error like error in missing(:) wrong spelling etc this is called compile time error)

# run time error(e.g something divide by zero)
# logical error(if a program give the output but the output is not of the user demond let you want to add two no 3 and 2 give 5 but its output is (let suppose 4) this is called logical error this is called logical error
# there are two types of statements (normal statement which give no error and normally execute the other one is critical statement which gives an error let suppose divide 5 by zero(0)
#a=5
#b=2
#try:
 #  print(a/b)


#except Exception:
    # except block is only execute when you have an error in the statement like any digit divide by zero

 #print("you cannot divide a number by zero")
#print("hello every one")

#a=5
#b=0
#try:
#   print(a/b)

# if we want to know about the (ERROR) we can write (as)(e) after the exception like see below which also print the exception (given an error division by zero)
#except Exception as e:


# print("you cannot divide a number by zero",e)
#print("hello every one")


#a=5
#b=0
#try:
#   print("resource open")

 #  print(a/b)



#except Exception as e:


 #print("you cannot divide a number by zero",e)
       # finally block will be executed if we get error as well as if we dont get the error
#finally:
 #print("resource close")



a=5
b=2

try:
   print("resource open")

   print(a/b)
   k = int(input("enter your number:"))
   print(k)


except ZeroDivisionError as e:

    print("you cannot divide a number by zero", e)

except ValueError as e:
    print("invalid option")
# this except will execute all the exception
except Exception as e:
    print("something went wrong....")

finally:
    print("resource close")
