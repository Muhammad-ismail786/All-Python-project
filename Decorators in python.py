# you can change the behaviour of existing function by using the (decorator) function Also change it in run time and also at the compile time itself
def div(a,b):
    print(a/b)
def smart_div(func):
        def inner(a,b):
            if a<b:
                a,b=b,a
            return func(a,b)          # actually the result is (0.5) but due to use of decorator func or operator we get the result (2) bcz using dcrt func change the behaviour of the function

        return inner
div=smart_div(div)


div(2,4)
