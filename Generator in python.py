#Generators are better for huge loops, as they only "hold" one value at the time.

# but iterator will "hold" all value at a time and stored it in a memory if we need a value one by one from database to read or gain one by one we can use generator instead of iterator

#What is difference in yield and return in Python?
#Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don't want to store the entire sequence in memory. Yield are used in Python generators.
#def topten():


  #  return 5
#values=topten()
#print(values)

def topten():





    n=1
    while n<=10:
        sq=n*n

        yield sq
        # the yield will return value one by one
        # why we use a generator bcz when we fetch let suppose hundred record from data base we one to work with one value at a time in this case we can use a generator(to fetch value one by one)
        # this is how we can use a generator with the use of the key word(yield)
        n+=1

value=topten()



for i in value:

    print(i)

