print("I will add up the numbers you give me.")
number=0
num=int(input("enter the number"))
while num!=0:
    number += num
    print("the total so far is",number)
    num=int(input("enter the number"))
print("the total is",number)
