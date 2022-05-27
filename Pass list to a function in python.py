def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd






list=[1,2,3,4,5,6,7,8]
even,odd=count(list)
print("even:{} and odd:{}".format(even,odd))
#print(odd)