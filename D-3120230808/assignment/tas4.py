password=input("password must contains at least one uppercase letter, one lowercase letter,and one digit :")
pass_word=len(password)
# if password==any(password.isupper()) and password==any(password.islower()) and password==any(password.isdigit()):
def strength():
    if pass_word<6:
        condition="weak"
    elif pass_word>=6 and pass_word<=10 :
        condition="moderate"
    elif pass_word>=11 and pass_word<=15 :
        condition= "strong"
    elif pass_word>15 :
        condition="very strong"
    return condition        
    # print(password(pass_word))
    
digit=False
upper=False
lower=False
for i in password:
    if i.islower():
        digit=True
    elif i.isupper():
        upper=True
    elif i.isdigit():
        lower=True

if digit==True and upper==True and lower==True:
    pass_word=strength()
    print(pass_word)
else:
    print("another password")
