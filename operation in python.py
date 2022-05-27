Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=10
y=12
x+y
22
x-y
-2
x*y
120
x/y
0.8333333333333334
Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax
the above is the arithematic operator
SyntaxError: invalid syntax
#assignment operator
x=x+2
x
12
#in short way
x+=2
x
14
x*=3
x
42
#we assign two value in one variable
x,y=4,5
x
4
y
5
#unary operator
n=7
n
7
n=-n
n
-7
n
-7
n
-7
n
-7
n=8
n
8
#single=means we are assign one value to other but ==equal means we are compaqring the two value
#rational operator
a<b
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a<b
NameError: name 'a' is not defined
a<b
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a<b
NameError: name 'a' is not defined
a=10
b=5
a<b
False
a>b
True
a==b
False
b=10
a==b
True
a<=b
True
a>=
SyntaxError: invalid syntax
a=>b
SyntaxError: invalid syntax
a>=b
True
a!=b
False
b=10
a!=b
False
a=10
b=10
a!=b
False
a=10
b=7
a!=b
True
#logical operator
#3 operator are logical operator#AND #OR#NOR
#AND#OR#NOT
a=5
b=4
a<6 and b>3
True
a<2 and b>3
False
#if both the condition is true the result is true #here we use AND operator
a<2 or b>3
True
a>4 or b<2
True
#if one condition is true the result is true here we use #OR operator
x=True
x
True
x=not true
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x=not true
NameError: name 'true' is not defined. Did you mean: 'True'?
x=not True
x
False
#NOT reverse the result of the operation
#let see the example
x=True
x
True
x=not True
x
False
x=False
x
False
x=not False
x
True
