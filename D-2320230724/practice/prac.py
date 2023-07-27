# swaplist
def swaplist(number):
    number[1],number[3]=number[3],number[1]
    return number
number=[1,5,10,15,20]
print(swaplist(number))

# average of a set of integers
# count=int(input("enter the count :"))
count=0
sum=0
# for i in range(count):
while (count<3):
    x=int(input("enter the numbers :"))
    count=count+1
    sum=sum+x
avg=sum/3
print(avg)


# sum of digits is an even number
for i in range(100,200):
    num=i
    sum=0
    while(num!=0):
        digit=num%10
        sum=sum+digit
        num=num/10
    if (sum%2==0):
        print(i)


