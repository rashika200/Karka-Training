n=int(input("enter the number :"))
num=0
num2=1
for i in range(0,n+1):
#     # print(i)
    number=num+num2
    # number=i+number
    num,num2=num2,number
    # print(number)
    if number<n:
        print(number,end=" ")


