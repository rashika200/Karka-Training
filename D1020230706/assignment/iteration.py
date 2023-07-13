numbers=[500,200,700,1000]
total_numbers=0
enum_numbers=enumerate(numbers)
print(type(enum_numbers))
for i,number in enum_numbers:
    print("entering iteration process for item#:"+str(i))
    print("before sum",total_numbers)
    total_numbers=total_numbers+number
    print("after sum",total_numbers)
    print("existing iteration process for item#:"+str(i))
    print("\n")


average=total_numbers/len(numbers)
print(average)


amounts=[500,200,700,1000]
a=[]
for i, amount in enumerate(numbers):
    b="INR "+str(amount)
    a.append(b)
print(a)