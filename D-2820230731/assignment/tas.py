numbers=[1,5,3,7,9,13]
number=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==10):
            number=+i
            number=+j
            print(number)



n=int(input("enter the number :"))