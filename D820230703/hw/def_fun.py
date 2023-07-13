num1=int(input("enter the first number"))
operator=input("enter the operator")
num3=int(input("enter the third number"))
def number(num1,operator,num3):
    if (operator=="+"):
        sum=num1+num3
        return sum
    elif (operator=="-"):
        sub=num1-num3
        return sub
    elif (operator=="*"):
        muli=num1*num3
        return muli
    elif (operator=="/"):
        div=num1/num3
        return div
    elif (operator=="%"):
        modul=num1%num3
        return modul
    elif (operator=="**"):
        power=num1**num3
        return power
    else:
        return ("no operator found")
calculation=number(num1,operator,num3)
print(calculation)
