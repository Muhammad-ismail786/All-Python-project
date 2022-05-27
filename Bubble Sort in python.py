

def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp





num=[4,5,7,2,3]
sort(num)
print(num)