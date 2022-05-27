# none 
#numeric e.g int, float, complex, bool
num=2.5
print(num)
type(num)
nums=2.5
nums
2.5
type(num)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(num)
NameError: name 'num' is not defined. Did you mean: 'nums'?
type(nums)
<class 'float'>
a=2.4
b=int(a)
b
2
type(b)
<class 'int'>
k=4
c=float(k)
c
4.0
b=complex(k,c)
b
(4+4j)
a=20
a
20
b=10
b
10
bool=a>b
bool
True
false=b>a
false
False
type(bool)
<class 'bool'>
int(true)

    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(bool)
1
int(true)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0
lst=[1,2,34,56,43,87]
lst
[1, 2, 34, 56, 43, 87]
type(lst)
<class 'list'>
t=[34,56,78,65,43,23]
t
[34, 56, 78, 65, 43, 23]
type(t)
<class 'list'>
s=[23,45,54,32]
s
[23, 45, 54, 32]
type(s)
<class 'list'>
s={23,45,56,78}
s
{56, 45, 78, 23}
type(s)
<class 'set'>
t=(23,41,12,1,3)
t
(23, 41, 12, 1, 3)
type(t)
<class 'tuple'>
str="ismail"
str
'ismail'
print(str)
ismail
type(str)
<class 'str'>
range(0,10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(2,10,20)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    list(2,10,20)
TypeError: list expected at most 1 argument, got 3
list(range(2,20,2)
     list
     
SyntaxError: '(' was never closed
list(range(2,20,2))
     
[2, 4, 6, 8, 10, 12, 14, 16, 18]
list(rang(21,3))
     
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    list(rang(21,3))
NameError: name 'rang' is not defined. Did you mean: 'range'?
d={'ismail':iphone,'gohar':samsung,'soban':realme}
     

     
SyntaxError: invalid syntax
d={'ismail':'samsung','soban':'iphone','gohar':'realme'}
     
d
     
{'ismail': 'samsung', 'soban': 'iphone', 'gohar': 'realme'}
d.keys()
     
dict_keys(['ismail', 'soban', 'gohar'])
d.values()
     
dict_values(['samsung', 'iphone', 'realme'])
d.get("ismail')
      

      

      
samsung
none,list,tupple,set,string,range,dictionary
