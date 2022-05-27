


def sort(num):
    for i in range(5):
        min=i
        for j in range(0,5):
            if num[j]<num[min]: # IT IS IN DECENDING ORDER FOR ASSENDING ONLY CHANGE THE SIGN TO GREATER(>)
                min=j
                temp=num[i]
                num[i]=num[min]
                num[min]=temp
                print(num) # for cheaking itteration






num=[4,5,7,2,3]
sort(num)
print(num)