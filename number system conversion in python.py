Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
convert decimal no to binary
SyntaxError: invalid syntax
#the base of decimal is 10 and the base of binary is 2
x=25
x
25
bin(25)
'0b11001'
ob0101
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ob0101
NameError: name 'ob0101' is not defined
ob0101
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ob0101
NameError: name 'ob0101' is not defined
0b0101
5
ob111
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ob111
NameError: name 'ob111' is not defined
ob01101
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ob01101
NameError: name 'ob01101' is not defined
0b01101
13
oct(25)
'0o31'
0o31
25
hex(25)
'0x19'
0x19
25
hex(10)
'0xa'
hex(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    hex(f)
NameError: name 'f' is not defined
0xf
15
110011010
110011010
bin(110011010)
'0b110100011101010001010000010'
0b110011010
410
a=15
b=12
x=(a//4+b**3)<2000 and (b%4!=0)
x
False
b=12
b%4
0
b%4!=0
False
