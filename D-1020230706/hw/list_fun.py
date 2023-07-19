def largest(list):
    largest=list[0]
    for i in list:
        if i>largest:
            largest=i
    return largest
list=[1,100,300,4]   
print("largest number=",largest(list))     




