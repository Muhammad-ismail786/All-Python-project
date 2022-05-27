import demo
print("its time to calculate")
#Unlike other programming languages, python is not designed to start execution of the code from a main function explicitly. A special variable called __name__ provides the functionality of the main function. As it is an in-built variable in python language, we can write a program just to see the value of this variable as below.

#print type(__name__)
#print __name__
#Running the above code gives us the following result −

#<type 'str'>
#__main__
#As you can see above the value of the __name__ variable is of string data type and equals to ___main__.

#Below are the two key features of __name__ variable.

#1. When you run any well-written stand-alone python script which is not referring to any other script, the value of __name__ variable is equal to __main__.

#Let's write a program named standalone.py to illustrate this feature.

#def func1():
  # print 'The value of __name__ is ' + __name__
#if __name__ == '__main__':
#   func1()
#Running the above code gives us the following result −

#The value of __name__ is __main__
#As expected the __name__ variable evaluates to __main__ hence the output.

#2. The second feature is about importing one python script into another. In such a scenario, there seem to be two different scopes which can be considered as the main() function. The first scope can be the __main__ variable of the currently running program and the second the scope of the __main__ variable of the imported script used in the current program.

#So which __main__ variable will be used

#when you run a function from the imported script, the __name__ variable will evaluate to the actual name of the script and not equal to __main__.

#But when you find out the value of the name variable from the current program, without referring to the imported script, it will evaluate to __main__ as expected, as that is the scope of the program at level 0 indention.

#The below program illustrates this example.

#Example
#import standalone as sa

#print('Running the imported script')
#sa.func1()

#print('\n')
#print('Running the current script')
#print 'The value of __name__ is ' + __name__
#Output
#Running the above code gives us the following result −

#Running the imported script
#The value of __name__ is standalone

#Running the current script
#The value of __name__ is __main__
#The usefulness of this approach is when the code if __name__ == "__main__": is used, the python interpreter checks if it's parsing the currently executed script, or if it's temporarily parsing another external script. This way the programmer has the ability to control the behaviors of different parts of the program by choosing to run lines of code from the external script as well as the currently executed script depending on the scenarios.
