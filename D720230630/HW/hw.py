# voting age
age=int(input("what is the age for voting"))
if ((age>=18)):
        print("you are eligible for voting")
else:
        print("you are not eligible for voting")   



# checking odd or even number
num=int(input("whether it is even or odd number")) 
if (num%2)==0:
    print("this is an even number")
else:
    print("this is an odd number")   


# getting golden token or silver token
item1=int(input("amount of first item"))
item2=int(input("amount of second item"))
item3=int(input("amount of third item"))
item4=int(input("amount of fourth item"))
items=(item1+item2+item3+item4)
if (items>=500 and items<1000):
        print("you have won silver token")    
elif (items>1000):
        print("you have won golden token")
else:
        print("you have no token")         



# getting bio-data
name=input("what is your name")   
age=int(input("what is your age"))
DOB=input("what is your dob")
college=input("what is your college name")
location=input("when is your college located")
print("hello,my name is",name,".Iam",age,"years old and was born on",DOB,".Currently,Iam located in",location,"and I completed my degree at",college,)