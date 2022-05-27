import sys

sys.setrecursionlimit(20)
print(sys.setrecursionlimit(20))
i=0
def great():
    global i
    i+=1
    print("hello",i)
    great()




great()