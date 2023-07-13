# simple interest
p=1000
n=10
r=2
def cal_interest(principal,number_of_years,rate_of_interest):
    interest=principal*number_of_years*rate_of_interest/100
    return interest
interest=cal_interest(p,n,r)
print(interest)




# twice number
num1=5
def twice(num1):
    num2=2*num1
    return num2
num2=twice(num1)
print(num2)




# eligible or not
passed_out_year=2023
def cal_eligible(passed_out_year):
    eligible=passed_out_year>2022
    return eligible
eligible=cal_eligible(passed_out_year)
print(eligible)



# string interpolation
age=21
txt=f"my name is Rashika,iam{age}"
print(txt)


age=21
txt="my name is rashika,iam"+ str(age)
print(txt)


# slicing
amount="USD 1000"
currency=amount[0:2]
print(currency)
currency=amount[4:]
print(currency)
l=len(amount)
print(l)
amount1=amount.lower()
print(amount1)


amount="USD 1000"
amount1=amount.strip()
print(amount1)
amount1=amount.replace(" ",".")
print(amount1)




txt="my name is rashika,iam 21"
txt1=txt.startswith("my")
print(txt1)
txt1=txt.endswith(".")
print(txt1)
txt1=txt.title()
print(txt1)




amount="USD 1000"
amount1=amount.isdigit()
print(amount1)
amount1=amount.isalpha()
print(amount1)
amount1=amount.isprintable()
print(amount1)
amount1=amount.encode()
print(amount1)
amount1=amount.expandtabs()
print(amount1)
amount1=amount.isalnum()
print(amount1)
amount="USD 1000"
print(amount.zfill(10))
txt="1000"
txt1=txt.center(0)
print(txt1)
txt="h*e*l*l*O"
txt1=txt.expandtabs(3)
print(txt1)
txt="hello,welcome to my world"
txt1=txt.index("welcome")
print(txt1)
txt1=txt.encode()
print(txt1)
mytable=str.maketrans("o","s")
print(txt.translate(mytable))
txt="bannana"
x=txt.ljust(20)
print=(x,"is my favourite fruit.")